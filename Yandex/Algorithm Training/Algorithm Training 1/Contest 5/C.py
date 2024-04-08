fin = open('input.txt')

N = int(fin.readline())
mountins = [0]*N
for i in range(N):
    _, y = [int(x) for x in fin.readline().split()]
    mountins[i] = y
      
prefix_straitward = [0]*(N+1)
prev = 0
for i in range(N):
    delta = mountins[i]-prev
    prefix_straitward[i+1] = delta+prefix_straitward[i] if delta > 0 else prefix_straitward[i]
    prev = mountins[i]

prefix_backward = [0]*(N+1)
prev = 0
for i in range(N):
    delta = mountins[N-i-1]-prev
    prefix_backward[N-i-1] = delta+prefix_backward[N-i] if delta > 0 else prefix_backward[N-i]
    prev = mountins[N-i-1]
    
M = int(fin.readline())
traces = [0]*M
for i in range(M):
   traces[i] = [int(x)-1 for x in fin.readline().split()]
   
delta_h = [0]*M
for i in range(M):
    if traces[i][0] <= traces[i][1]:
        delta_h[i] = prefix_straitward[traces[i][1]+1]-prefix_straitward[traces[i][0]+1]
    else:
        delta_h[i] = prefix_backward[traces[i][1]]-prefix_backward[traces[i][0]]

print(*delta_h, sep='\n')