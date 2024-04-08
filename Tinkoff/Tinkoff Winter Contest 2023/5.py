import sys
import math

def addNumber(curr_peak, number, start_num, add_num, friends, heavy_peaks):
    if heavy_peaks[curr_peak]:
        add_num[curr_peak] += number
    else:
        for next_peak in friends[curr_peak]:
            start_num[next_peak] += number

def getNumber(curr_peak, start_num, add_num, heavy_friends):
    next_nums = 0
    for next_peak in heavy_friends[curr_peak]:
        next_nums += add_num[next_peak]

    return start_num[curr_peak]+next_nums

# fin = open('input.txt')
fin = sys.stdin

N, M, Q = [int(x) for x in fin.readline().split()]
start_num = [int(x) for x in fin.readline().split()]
add_num = [0]*N

friends = [[] for _ in range(N)]
for i in range(M):
    U, V = [int(x) for x in fin.readline().split()]
    friends[U-1].append(V-1)
    friends[V-1].append(U-1)

root_E = int(math.sqrt(N))
heavy_peaks = [False]*N
for i in range(N):
    friends_num = len(friends[i])
    if friends_num >= root_E: heavy_peaks[i] = True

heavy_friends = [[] for _ in range(N)]
for i in range(N):
    for friend in friends[i]:
        if heavy_peaks[friend]: heavy_friends[i].append(friend)
   
for _ in range(Q):
    event = [x for x in fin.readline().split()]
    if event[0] == '+':
        curr_peak = int(event[1])-1
        number = int(event[2])
        addNumber(curr_peak, number, start_num, add_num, friends, heavy_peaks)
    elif event[0] == '?':
        curr_peak = int(event[1])-1
        print(getNumber(curr_peak, start_num, add_num, heavy_friends))