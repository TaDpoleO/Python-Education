import heapq

fin = open('transfer.in')
N, M = [int(x) for x in fin.readline().split()]

graph = [[] for _ in range(N+1)]
for i in range(M):
    point1, point2, t, w = [int(x) for x in fin.readline().split()]
    graph[point1].append((point2, t, w))
    graph[point2].append((point1, t, w))

def getRoadTime(graph, cup_number):
    if cup_number == 0: return 0

    CAR_WEIGHT = 3000000
    CUP_WEIGHT = 100

    cross_time = [float('inf')]*(N+1)
    cross_time[1] = 0

    total_weight = cup_number*CUP_WEIGHT+CAR_WEIGHT    
    stack, visited = [(0, 1)], set()
    while stack:
        curr_time, curr_point = heapq.heappop(stack)
        
        if curr_point not in visited:
            for next_point, next_time, next_weight in graph[curr_point]:
                if total_weight <= next_weight and curr_time+next_time < cross_time[next_point]:
                    cross_time[next_point] = curr_time+next_time
                    heapq.heappush(stack, (curr_time+next_time, next_point))                    

        visited.add(curr_point)

    return cross_time[N]

def bsearch(graph, left, right):
    while left < right:
        mid = (left+right+1)//2
        # TTFF
        if getRoadTime(graph, mid) <= 1440:
            left = mid
        else:            
            right = mid-1

    return left

print(bsearch(graph, 0, 10000000))