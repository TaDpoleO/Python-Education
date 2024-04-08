from collections import defaultdict, deque

fin = open('input.txt')
N = int(fin.readline())

genealogy_tree, sons, parents = defaultdict(list), set(), set()
for _ in range(N-1):
    son, parent = fin.readline().split()
    genealogy_tree[parent].append(son)
    sons.add(son)
    parents.add(parent)

sons_level = dict()

stack = deque([((parents-sons).pop(), 0)])
while stack:
    man, level = stack.pop()
    sons_level[man]=level

    for son in genealogy_tree[man]:
        stack.appendleft((son, level+1))

for son in sorted(sons_level.keys()):
    print(f'{son} {sons_level[son]}')