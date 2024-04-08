def bsearch_left(prefix, target):    
    left = 0
    right = len(prefix)-1

    while left < right:
        mid = (left+right)//2
        # FFFF, TTTT, FFTT
        if prefix[mid][0] >= target:
            right = mid
        else:
            left = mid+1

    if prefix[left][0] < target: left += 1
    if left == 0: left = 1
    return left

def bsearch_right(prefix, target):    
    left = 0
    right = len(prefix)-1

    while left < right:
        mid = (left+right+1)//2
        # FFFF, TTTT, TTFF
        if prefix[mid][0] <= target:
            left = mid
        else:
            right = mid-1

    return left

def getSegmentValue(prefix, start, end):
    if start <= prefix[-1][0] and end >= prefix[1][0]:
        start_index = bsearch_left(prefix, start)
        end_index = bsearch_right(prefix, end)

        return prefix[end_index][1]-prefix[start_index-1][1]
    else:
        return 0

fin = open('input.txt')

N = int(fin.readline())
orders = [(0, 0, 0)]*N

for i in range(N):
    orders[i] = [int(x) for x in fin.readline().split()]
    
prefix_cost_of_starts = [(0, 0)]
orders.sort(key=lambda x: x[0])
for start, _, cost in orders:
    if prefix_cost_of_starts[-1][0] != start:
        prefix_cost_of_starts.append((start, prefix_cost_of_starts[-1][1]+cost))
    else:
        prefix_cost_of_starts[-1] = (prefix_cost_of_starts[-1][0], prefix_cost_of_starts[-1][1]+cost)         
      
prefix_duration_of_ends = [(0, 0)]
orders.sort(key=lambda x: x[1])
for start, end, _ in orders:
    if prefix_duration_of_ends[-1][0] != end:
        prefix_duration_of_ends.append((end, prefix_duration_of_ends[-1][1]+end-start))
    else:
        prefix_duration_of_ends[-1] = (prefix_duration_of_ends[-1][0], prefix_duration_of_ends[-1][1]+end-start)

Q = int(fin.readline())
answer = [0]*Q
for i in range(Q):
    start, end, query_type = [int(x) for x in fin.readline().split()]
    
    if query_type == 1:
        answer[i] = getSegmentValue(prefix_cost_of_starts, start, end)
    elif query_type == 2:
        answer[i] = getSegmentValue(prefix_duration_of_ends, start, end)

print(*answer)