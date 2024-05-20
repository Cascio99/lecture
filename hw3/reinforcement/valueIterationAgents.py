# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        "### V(s) = max_{a in actions} Q(s,a) ###"
        # print(self.values)
        # print(self.mdp.getStartState())
        # print(self.values[self.mdp.getStartState()])
        # print('ALL states: ',self.mdp.getStates())
        for k in range(1, self.iterations+1):
            # last fix: crucial for updating values at each iteration?! 1ST NOTE in instruction: "must use ith values at i+1th iteration"
            tmp_values = self.values.copy()
            # print(k,"th iteration...\n")
            for s in self.mdp.getStates():
                if self.mdp.isTerminal(s):
                    continue    # handling TERMINAL_STATE
                if k>1 and self.mdp.getPossibleActions(s)==('exit',):
                    continue    # skip EXIT_STATES(state of exit-to-terminal: technically non-terminals): unnecessary-code(faster algorithm)
                # pi = None # debug
                max = -10000000 #-inf
                for a in self.mdp.getPossibleActions(s):
                    tmp = self.getQValue(s, a)
                    if tmp > max:
                        max = tmp
                        # pi = a
                tmp_values[s] = max
                # self.values[s] = max  # wrong code
                # print('for state ',s,' finished. value: ',tmp_values[s],'by choosing ',pi,'\n')
            # update self.values
            for s in self.mdp.getStates():
                self.values[s] = tmp_values[s]  # last fix: from `self.values[s] = max` above
            # print(k,'th iteration finished\n')
            
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        sum = 0
        for pair in self.mdp.getTransitionStatesAndProbs(state, action):
            nextState, prob = pair
            r = self.mdp.getReward(state, action, nextState)
            gamma = self.discount
            v = self.values[nextState]
            "### Q(s,a) = sum_s'{T(s,a,s')*[R(s,a,s') + gamma*V_k(s')]} ###"
            # print('T, R, V: ',prob,r,v,'\n')
            # print('state: ',state,', action canditate: ',action,'\n')
            sum += prob*(r + gamma*v)
        return sum
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        "### policy(s) = arg_max_{a in actions} Q(s,a) ###"
        if self.mdp.isTerminal(state):
            return None
        pi = None
        max = -10000000
        for a in self.mdp.getPossibleActions(state):
            tmp = self.getQValue(state, a)
            if tmp > max:
                max = tmp
                pi = a
        return pi
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class PrioritizedSweepingValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        # compute predecessors of all states
        pre = set()
        for s in self.mdp.getStates():
            pre.add(s)
            for p in self.mdp.getStates():
                for a in self.mdp.getPossibleActions(p):
                    for pair in self.mdp.getTransitionStatesAndProbs(p, a):
                        if pair[1] == 0:
                            continue    # predecessor's property: prob>0
                        if pair[0] != s:
                            continue    # predecessor's definition: T(p,a)=s
                        pre
        Q = util.PriorityQueue()
        for s in self.mdp.getStates():
            if not self.mdp.isTerminal(s):
                continue
            s_current = self.values[s]
            s_highest = -10000000 # -inf
            for a in self.mdp.getPossibleActions(s):
                tmp = self.getQValue(s, a)
                if tmp > highestQValue:
                    highestQValue = tmp
            diff = abs(s_current - s_highest)   # don't update self.values[s] here
            Q.push(s, -diff)
            for i in range(self.iterations):
                if Q.isEmpty():
                    return
                s = Q.pop()
                if not self.mdp.isTerminal(s):
                    self.values[s] = diff
                for p in self.mdp.getStates():
                    for a in self.mdp.getPossibleActions(p):
                        for pair in self.mdp.getTransitionStatesAndProbs(p, a):
                            if pair[1] == 0:
                                continue    # predecessor's property: prob>0
                            if pair[0] != s:
                                continue    # predecessor's definition: T(p,a)=s
                            p_current = self.values[p]
                            p_highest = -10000000
                            for a in self.mdp.getPossibleActions(p):
                                temp = self.getQValue(p, a)
                                if temp > p_highest:
                                    p_highest = temp
                            diff = abs(p_current - p_highest)
                            if diff > self.theta:
                                Q.update(p, -diff)