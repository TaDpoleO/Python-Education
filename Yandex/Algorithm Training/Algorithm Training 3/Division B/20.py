import heapq

fin = open('input.txt')
N = int(fin.readline())

numbers = [int(x) for x in fin.readline().split()]
heapq.heapify(numbers)

answer = []
while len(numbers) > 0:    
    answer.append(heapq.heappop(numbers))
    
print(*answer)