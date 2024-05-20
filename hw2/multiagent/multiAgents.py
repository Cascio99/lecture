# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        # print('choose next action: ',legalMoves[chosenIndex],'by score: ',bestScore)

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # print('after action', action, ': ', manhattanDistance(newPos, random.choice(newFood.asList())))
        # print(newGhostStates[0].getPosition())

        # 1st feature: reciprocal of 'distance of pacman ~ food'
        f_1 = 1
        min = 0x77777777
        for nextFood in newFood.asList():
            if min > manhattanDistance(newPos, nextFood):
                min = manhattanDistance(newPos, nextFood)
                f_1 = 1 / manhattanDistance(newPos, nextFood)

        # 2nd feature: distance of pacman ~ ghost
        f_2 = 0
        for e in newGhostStates:
             f_2 += manhattanDistance(newPos, e.getPosition()) # e: newGhostStates[0], newGhostStates[1], ...

        # 3rd feature: next game state' score
        f_3 = successorGameState.getScore()

        # 4th feature: ghosts' scared times
        f_4 = newScaredTimes[0]

        if f_4 > 0:
            f_2 *= -1

        # linear combinations of features
        "test weight: w_1 = 30 -> 10, w_2 = 1 -> 1, w_3 = 10 -> 0.1, w_4 = 1 -> 1"
        eval = 1*f_1 + 0.03*f_2 + 0.3*f_3 + 0.1*f_4
        #print('Move ', action, ': ', 1*f_1, 0.03*f_2, 0.3*f_3, 0.1*f_4, 'eval: ', eval)
        return eval

        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # Pi(s) = arg_a(V(s')): a in s.actions
        # generate all minimax game-states by GameState.genSucc() or getAct() --> means GameState.getLegalActions()?
        def val(state: GameState, agent_idx, cur_level):
            # game terminated. not by minimax_depth_limitation
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            # more than 3 agents?
            next_agent_idx = (agent_idx+1)%state.getNumAgents()

            # leaf
            if cur_level == state.getNumAgents()*self.depth+1:
                cur_level -= 1
                return self.evaluationFunction(state)
            # max-node: pacman
            elif agent_idx==0:
                best = -10000000
                for a in state.getLegalActions(agent_idx):
                    next_val = val(state.generateSuccessor(agent_idx,a), next_agent_idx, cur_level+1)    # pacman's succ: ghost#0
                    if next_val > best:
                        best = next_val
                return best
            # min-node: ghost
            elif agent_idx!=0:
                best = 10000000
                for a in state.getLegalActions(agent_idx):
                    next_val = val(state.generateSuccessor(agent_idx,a), next_agent_idx, cur_level+1)
                    if next_val < best:
                        best = next_val
                return best

        # minimax_decision
        def minimax_decision():
            # how to check state.is_leaf? --> cur_lev: current expanded level
            cur_lev = 1    # level limitation => (agents#)*depth
            act = Directions.EAST   # default action
            best = -10000000
            for a in gameState.getLegalActions(self.index):  # pacman at the root(max-node) state
                # 2nd parameter: next agent index, 3rd parameter: next level=2 ( initial level=1)
                next_val = val(gameState.generateSuccessor(self.index,a), self.index+1, cur_lev+1)
                if next_val > best:
                    best = next_val
                    act = a
            return act

        # print(gameState.getNumAgents())
        # print(gameState.generateSuccessor(0,Directions.EAST))
        return minimax_decision()
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def val(state: GameState, agent_idx, cur_level, alpha, beta):
            # game terminated. not by minimax_depth_limitation
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            # more than 3 agents?
            next_agent_idx = (agent_idx+1)%state.getNumAgents()

            # leaf
            if cur_level == state.getNumAgents()*self.depth+1:
                cur_level -= 1
                return self.evaluationFunction(state)
            # max-node(pacman): pruning by Comparing with beta & Updating alpha
            elif agent_idx == 0:
                # print("Root node ")
                best = -10000000
                for a in state.getLegalActions(agent_idx):
                    next_val = val(state.generateSuccessor(agent_idx,a), next_agent_idx, cur_level+1, alpha, beta)    # pacman's succ: ghost#0
                    if next_val > best:
                        best = next_val
                    # expand minimax to AlphaBeta: def val(state,agent_idx,cur_level,alpha,beta)
                    # how to roll_back alpha & beta????
                    # 1st try) alpha = -infinite, beta = infinite?
                    if next_val > beta:     # pruning   # 6-tied-root? --> fixed from "if next_val >= beta" --> still misterious...
                        # print(alpha)
                        # roll_back alpha before backtracking
                        alpha = -10000000
                        return next_val
                    if next_val > alpha:    # update alpha
                        alpha = next_val

                # roll_back alpha before backtracking
                alpha = -10000000
                return best
            # min-node(ghost): pruning by Comparing with Alpha-value & Updating beta
            elif agent_idx != 0:
                best = 10000000
                for a in state.getLegalActions(agent_idx):
                    # consider the time of generating nodes....
                    next_val = val(state.generateSuccessor(agent_idx,a), next_agent_idx, cur_level+1, alpha, beta)
                    if next_val < best:
                        best = next_val

                    if next_val < alpha:    # failed 6-tied-root? --> fixed from "if next_val >= alpha" --> still curious...
                        # roll_back beta before backtracking
                        # improved for ghost-agents ==> if only when it's the last_index of ghost_agent
                        if(agent_idx == state.getNumAgents()-1):
                            beta = 10000000
                        return next_val
                    if next_val < beta:
                        beta = next_val

                # roll_back beta before backtracking
                # improved for ghost-agents ==> only if when it's the last_index_ghost_agent
                if(agent_idx == state.getNumAgents()-1):
                    beta = 10000000
                return best

        # alphabeta_pruning
        def alphabeta_pruning(): # max-val among the root's successors
            # how to check state.is_leaf?
            cur_lev = 1    # level = (agents#)*depth
            act = Directions.EAST   # default action
            best = -10000000
            
            # couldn't apply alpha-pruning at root(max-node) --> similar logic in max-val()
            alpha_r = -10000000 # @root: unnecessary 
            beta_r = 10000000
            for a in gameState.getLegalActions(self.index):  # pacman at the root(max-node) state
                # 2nd parameter: next agent index, 3rd parameter: next level=2 ( initial level=1 )
                next_val = val(gameState.generateSuccessor(self.index,a), self.index+1, cur_lev+1, alpha_r, beta_r)
                if next_val > best:
                    best = next_val
                    act = a

                if next_val > beta_r:   # failed 6-tied-root? --> fixed from "if next_val >= beta_r" --> still curious...
                    # alpha_r = -10000000  # @root: unnecessary
                    return act
                if next_val > alpha_r:  # mistake: fixed from "elif next_val > alpha_r"....
                    alpha_r = next_val
                
            # alpha_r = -10000000  # @root: unnecessary
            return act

        return alphabeta_pruning()
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        # generate all minimax game-states by GameState.genSucc() or getAct() --> means GameState.getLegalActions()?
        def val(state: GameState, agent_idx, cur_level):
            # game terminated. not by minimax_depth_limitation
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state)
            # more than 3 agents?
            next_agent_idx = (agent_idx+1)%state.getNumAgents()

            # leaf
            if cur_level == state.getNumAgents()*self.depth+1:
                cur_level -= 1
                return self.evaluationFunction(state)
            # max-node: pacman
            elif agent_idx==0:
                best = -10000000
                for a in state.getLegalActions(agent_idx):
                    next_val = val(state.generateSuccessor(agent_idx,a), next_agent_idx, cur_level+1)    # pacman's succ: ghost#0
                    if next_val > best:
                        best = next_val
                return best
            # expect-node: ghost
            elif agent_idx!=0:
                best = 10000000
                i=0
                sum=0
                for a in state.getLegalActions(agent_idx):
                    sum += val(state.generateSuccessor(agent_idx,a), next_agent_idx, cur_level+1)
                    i += 1
                # return average value
                return sum/i

        # expectimax_decision
        def expectimax_decision():
            # how to check state.is_leaf? --> cur_lev: current expanded level
            cur_lev = 1    # level limitation => (agents#)*depth
            act = Directions.EAST   # default action
            best = -10000000
            for a in gameState.getLegalActions(self.index):  # pacman at the root(max-node) state
                # 2nd param: next agent index, 3rd parameter: next level=2 ( initial level=1 )
                next_val = val(gameState.generateSuccessor(self.index,a), self.index+1, cur_lev+1)
                if next_val > best:
                    best = next_val
                    act = a
            return act

        return expectimax_decision()
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    # 1st feature: return currentGameState.getScore()
    f_1 = scoreEvaluationFunction(currentGameState)

    pacmanPos = currentGameState.getPacmanPosition()
    ghostPos = currentGameState.getGhostPositions()
    ghostNum = currentGameState.getNumAgents() - 1
    sum_dist = 0

    # 2nd f_: calculate average distance of pacman ~ ghost
    for i in range(0, ghostNum):
        sum_dist += manhattanDistance(pacmanPos,ghostPos[i])
    f_2 = sum_dist / ghostNum

    # 3rd feature: average distance from `each ghost to farthest food`?
    food_list = currentGameState.getFood()
    max = -1
    for food in food_list:
        tmp = 0
        for g in ghostPos:  # sum of distace from `each ghost~food``
            tmp += manhattanDistance(g,food)
        tmp
        if tmp > max:
            max = tmp
    if max == -1:
        max = 1
    f_3 = max / ghostNum

    # # 4th f_: has food?
    # f_4 = currentGameState.hasFood(pacmanPos[0],pacmanPos[1])
    # # distance from `pacman to closest food`
    # min = manhattanDistance(pacmanPos,food_list[0])
    # for food in food_list[1:]:
    #     tmp = 0
    #     tmp += manhattanDistance(pacmanPos,food)
    #     if tmp < min:
    #         min = tmp
    # if min == 0:
    #     min = 1
    # f_5 = 1/min
    # f_7 = -currentGameState.getNumFood()

    # test weight: w_1: 3, w_2: 2, w_3: 1 ==> ave score: 746.9
    return 3.0*f_1 + 2.0*f_2 + 1.0*f_3
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
