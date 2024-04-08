from collections import defaultdict, deque

fin = open('input.txt')
N, K = [int(x) for x in fin.readline().split()]

res_left, res_right, curr_min_length = 1, N, N
curr_tree_set, curr_trees, right = defaultdict(int), deque([]), 0

for tree in fin.readline().split():
    curr_trees.append(tree)
    curr_tree_set[tree] += 1
    right += 1

    while curr_tree_set[curr_trees[0]] > 1:
        curr_tree_set[curr_trees.popleft()] -= 1

    if len(curr_tree_set) == K:
        if len(curr_trees) < curr_min_length:
            res_left = right-len(curr_trees)+1
            res_right = right
            curr_min_length = len(curr_trees)
    
print(res_left, res_right)