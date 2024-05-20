import util

# pre = util.Counter()
# pre[(0,0)] = ((0,1))
# pre[(0,0)] = ((0,1),(1,0))
# pre[(0,0)] = ((0,1))
# print(pre)
# print(type(pre[(0,0)]))

# pre = util.Counter(set())

pre = set()
pre.add((0,0))
pre[(0,0)].add((0,1))

print(pre)