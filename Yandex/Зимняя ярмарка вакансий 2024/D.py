import heapq

fin = open('input.txt')

N, X = [int(x) for x in fin.readline().split()]
A = [int(x) for x in fin.readline().split()]

total_A = sum(A)
B = [0]*N
for i in range(N):
    B[i] = X*A[i]/total_A

R = [round(x) for x in B]

dRplus, dRminus = [], []
for i in range(N):
    if R[i] >= B[i]:
        heapq.heappush(dRplus, (-abs(R[i]-B[i]), i))
    else:
        heapq.heappush(dRminus, (-abs(R[i]-B[i]), i))


total = sum(R)

index = 0
while total != X:        
    if total > X:
        _, i = heapq.heappop(dRplus)
        R[i] -= 1
        total -= 1

        if R[i] >= B[i]:
            heapq.heappush(dRplus, (-abs(R[i]-B[i]), i))
        else:
            heapq.heappush(dRminus, (-abs(R[i]-B[i]), i))
    else:
        _, i = heapq.heappop(dRminus)        
        R[i] += 1
        total += 1

        if R[i] >= B[i]:
            heapq.heappush(dRplus, (-abs(R[i]-B[i]), i))
        else:
            heapq.heappush(dRminus, (-abs(R[i]-B[i]), i))        
    
print(*R)