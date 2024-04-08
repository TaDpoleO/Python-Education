fin = open('input.txt')
numbers = [int(x) for x in fin.readline().split()]

visited = set()
for num in numbers:
    if num in visited:
        print('YES')
    else:
        print('NO')
    
    visited.add(num)