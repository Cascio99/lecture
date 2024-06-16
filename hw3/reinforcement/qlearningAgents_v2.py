# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        self.qvalues = util.Counter()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        # how to check visit? --> unvisited states' Q-value: 0
        return self.qvalues[state, action]
        util.raiseNotDefined()


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        # V(s) = max_a{Q(s, a)}
        action = self.computeActionFromQValues(state) # choose random_action?
        if action == None:  # terminal_state
          return 0.0
        return self.getQValue(state, action)
        util.raiseNotDefined()

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        # choose random_action?
        if self.getLegalActions(state) == (): # terminal_state
          return None
        pi = None
        max = -10000000
        for action in self.getLegalActions(state):
          tmp = self.getQValue(state, action)
          if tmp > max:
            pi = action
            max = tmp
        return pi
        util.raiseNotDefined()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if legalActions == ():  # terminal_state
          return None
        # print(util.flipCoin(self.epsilon))
        # print(random.choice(legalActions))
        p = util.flipCoin(self.epsilon)
        # case 1: choose random_action
        if p == True:
          return random.choice(legalActions)
        # case 2: choose optimal_action for current episode
        max = -10000000
        for a in legalActions:
          tmp = self.getQValue(state, a)
          if tmp > max:
            action = a
            max = tmp
        return action
        util.raiseNotDefined()

        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        # Q(s, a) <- Q(s, a) + alpha*[R(s, a, s') + gamma*max_a'{Q(s', a')} - Q(s, a)]
        nextStateVal = self.getValue(nextState)
        sampleQ = reward + self.discount*nextStateVal
        self.qvalues[state, action] += self.alpha*(sampleQ - self.qvalues[state, action])
        # print('QValue of state ',state,', action ',action,': ',self.qvalues[state, action])
        return self.qvalues[state, action]
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        # fitting self.weights to self.featExtractor.getFeatures(state, action): util.Counter(util.Counter()) type
        "must link self.weights[i] to self.featExtractor.getFeatures(state, action)[i]"
        w = self.getWeights()
        f = self.featExtractor.getFeatures(state, action)
        return w.__mul__(f)
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        # i: 1 ~ n
        # w_i <- w_i + alpha*difference*f_i(s, a), difference = sampleQ-Q, sampleQ = R(s, a, s') + gamma*max_a'{Q(s', a')}
        nextStateVal = -10000000
        pi = None
        for a in self.getLegalActions(nextState):
          tmp = self.getQValue(nextState, a)
          if tmp > nextStateVal:
            nextStateVal = tmp
            pi = a
        if pi == None:  # terminal_state
          nextStateVal = 0
        sampleQ = reward + self.discount*nextStateVal
        diff = sampleQ - self.getQValue(state, action)
        w = self.getWeights()
        f = self.featExtractor.getFeatures(state, action)
        len = int(f.totalCount())
        sumQ = 0
        if len==4:  # CoordinateExtractor: 4 features for each {state, action} pair
          for i in range(len):  # hard_coding..?
            if i==0:
              sumQ += w[state, action]*f[state, action]
              self.weights[state, action] += self.alpha*diff*f[state, action]
            elif i==1:
              sumQ += w['x=%d'%state[0]]*f['x=%d'%state[0]]
              self.weights['x=%d'%state[0]] += self.alpha*diff*f['x=%d'%state[0]]
            elif i==2:
              sumQ += w['y=%d'%state[0]]*f['y=%d'%state[0]]
              self.weights['y=%d'%state[0]] += self.alpha*diff*f['y=%d'%state[0]]
            elif i==3:
              sumQ += w['action=%s'%action]*f['action=%s'%action]
              self.weights['action=%s'%action] += self.alpha*diff*f['action=%s'%action]
        else:   # only 1 feature for each {state, action} pair
          sumQ += w[state, action]*f[state, action]
          self.weights[state, action] += self.alpha*diff*f[state, action]
        delta = f.copy()
        if self.alpha!=0 and diff!=0:
          delta.divideAll(1/(self.alpha*diff))
          self.weights.__radd__(delta)
        # update QValues???
        # self.qvalues[state, action] = sumQ
        return self.getWeights()
        util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            # print('help')
            pass
