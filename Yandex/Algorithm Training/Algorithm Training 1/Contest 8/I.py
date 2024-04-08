from collections import defaultdict, deque

fin = open('input.txt')
N = int(fin.readline())

genealogy_tree, all_people = defaultdict(list), set()
for _ in range(N-1):
    son, parent = fin.readline().split()
    genealogy_tree[parent].append(son)
    all_people.add(son)
    all_people.add(parent)

people_map = dict()
for i, man in enumerate(all_people):
    people_map[i] = man
    people_map[man] = i

sons_number = dict()

stack = deque(range(N))
while stack:
    man = people_map[stack.pop()]
    if genealogy_tree[man] == []:
        sons_number[man] = 0
    else:
        count = len(genealogy_tree[man])
        for son in genealogy_tree[man]:
            if son in sons_number:
                count += sons_number[son]
            else:
                stack.appendleft(people_map[man])
                break
        else:
            sons_number[man] = count

for people in sorted(all_people):
    print(f'{people} {sons_number[people]}')