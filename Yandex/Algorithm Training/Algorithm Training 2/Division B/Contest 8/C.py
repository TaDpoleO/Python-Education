fin = open('input.txt')
N = int(fin.readline())

parents, sons = set(), set()
tree = dict()
for _ in range(N-1):
    son, parent = fin.readline().split()
    tree[son] = parent

def getGenericalParent(tree, name1, name2):
    ancestors = set([name1])

    curr_name = name1
    while curr_name in tree and tree[curr_name] in tree:
        ancestors.add(tree[curr_name])
        curr_name = tree[curr_name]

    generical_parent = name2
    while generical_parent in tree and generical_parent not in ancestors:
        generical_parent = tree[generical_parent]

    return generical_parent

for line in fin:
    name1, name2 = line.split()
    print(getGenericalParent(tree, name1, name2))