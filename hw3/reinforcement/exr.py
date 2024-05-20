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

sets[(0,0)] = cand
# print(sets.__getitem__((0,0)))
# print(sets.get((0,0)))
for p in sets.get((0,0)):
    print(p)
# print(sets)
# print(type(sets))
# print(type(sets[(0,0)]))

# print(1e-2)