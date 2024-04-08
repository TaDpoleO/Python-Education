from collections import defaultdict

fin = open('input.txt')
N = int(fin.readline())

tree = defaultdict(list)
for _ in range(N-1):
    son, parent = fin.readline().split()
    tree[parent].append(son)

answer = []
for line in fin:
    name1, name2 = line.split()

    res = 0
    stack = [name1]
    while stack:
        curr_name = stack.pop()

        for next_name in tree[curr_name]:
            if next_name == name2:
                res = 1
                break
            stack.append(next_name)
    
    if res == 0:
        stack = [name2]
        while stack:
            curr_name = stack.pop()

            for next_name in tree[curr_name]:
                if next_name == name1:
                    res = 2
                    break
                stack.append(next_name)

    answer.append(res)

print(*answer)