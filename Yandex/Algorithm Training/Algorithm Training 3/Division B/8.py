fin = open('input.txt')
K = int(fin.readline())

minX = minY = float('inf')
maxX = maxY = float('-inf')

for _ in range(K):
    x, y = [int(x) for x in fin.readline().split()]
    minX = min(minX, x)
    minY = min(minY, y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)

print(minX, minY, maxX, maxY)