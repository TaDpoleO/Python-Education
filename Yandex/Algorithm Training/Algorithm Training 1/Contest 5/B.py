fin = open('input.txt')

N, K = [int(x) for x in fin.readline().split()]
numbers = [int(x) for x in fin.readline().split()]

prefix_sum = [0]*(N+1)
for i in range(N):
    prefix_sum[i+1]=prefix_sum[i]+numbers[i]
    
left, right, count = 0, 0, 0
while right < N+1:
    curr_delta = prefix_sum[right]-prefix_sum[left]
    if curr_delta == K:
        count += 1

    if curr_delta > K:
        left += 1
    else:
        right += 1

print(count)