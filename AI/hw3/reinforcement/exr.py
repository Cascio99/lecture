import util

# pre = util.Counter()
# pre[(0,0)] = ((0,1))
# pre[(0,0)] = ((0,1),(1,0))
# pre[(0,0)] = ((0,1))
# print(pre)
# print(type(pre[(0,0)]))

# pre = util.Counter(set())

# sets = [set() for i in range(50)]
# sets[0].add((0,0))
# sets[0].add((0,0))

# sets = [set() for i in range(50)]
# sets.
sets = util.Counter(set())
cand = set()
cand.add((0,1))
cand.add((0,1))
cand.add((1,0))
cand.add((1,0))
cand.add((-1,0))
cand.add((-1,0))

sets[(0,0)] = cand
# print(sets.__getitem__((0,0)))
# print(sets.get((0,0)))
#for p in sets.get((0,0)):
#    print(p)
s = (0,0)
# for p in sets[s]:
#     print(p)
# print(sets)
# print(type(sets))
# print(type(sets[(0,0)]))

# print(1e-2)

# for Q5
qvalues = util.Counter()
state = (0,0)
action = 'west'
qvalues[state, action] = 0
qvalues[(1,1),'exit'] = 10
qvalues[(3,3),'east'] = 9.5
# print(type(qvalues))
# print(qvalues)
# sorted = qvalues.sortedKeys()
# print(sorted)

import random
actions = ['west','east','exit','north']
# print(random.choice(actions))

# Q9
from featureExtractors import *
from qlearningAgents import *
state = (0,0)
action = 'west'

i = IdentityExtractor()
# print(i.getFeatures(state, action).totalCount())
# print(i.getFeatures(state, action).__getitem__(1))
# print(i.getFeatures(state, action))

c = CoordinateExtractor()
# print(c.getFeatures(state, action).totalCount())
len = int(c.getFeatures(state, action).totalCount())
# for i in range(len):
#     # print(i)
#     if i==0:
#         print(c.getFeatures(state, action)[state])
#     elif i==1:
#         print(c.getFeatures(state, action)['x=%d'%state[0]])
    # print(c.getFeatures(state, action)[i])
# print(type(c.getFeatures(state, action)))
# print(type(c.getFeatures(state, action).__getitem__('x=0')))
# print(c.getFeatures(state, action))

c.getFeatures(state, action).divideAll(1/2)
print(c.getFeatures(state, action))