import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def answer(tree, peaks, interests):
    def check_node(curr_companies, interests):
        count = 0
        for company in interests:
            if curr_companies[company] > 0: count += 1
        
        return count == len(interests)

    def dfs(curr_peak, curr_price, curr_companies, tree, peaks, interests, result):
        if not tree[curr_peak]:
            if check_node(curr_companies, interests) and (curr_price < result[0]): result[0] = curr_price

        for next_peak in tree[curr_peak]:
            curr_companies[peaks[next_peak][1]] += 1
            dfs(next_peak, curr_price+peaks[next_peak][0], curr_companies, tree, peaks, interests, result)
            curr_companies[peaks[next_peak][1]] -= 1

    min_price = [float('inf')]
    curr_companies = defaultdict(int)

    curr_companies[peaks[0][1]] += 1
    dfs(0, peaks[0][0], curr_companies, tree, peaks, interests, min_price)

    if min_price[0] != float('inf'):
        return min_price[0]
    else:
        return -1

# fin = open('input.txt')
fin = sys.stdin

N, K = [int(x) for x in fin.readline().split()]
interests = set()
for i in range(K):
    interests.add(fin.readline().rstrip())

tree = [[] for _ in range(N)]
peaks = [(0, '')]*N
for i in range(N):
    P, A, C = [int(x) if i != 2 else x for i, x in enumerate(fin.readline().split())]
    if P != 0: tree[P-1].append(i)
    peaks[i] = (A, C)

print(answer(tree, peaks, interests))