fin = open('input.txt')

A = int(fin.readline().rstrip())
B = int(fin.readline().rstrip())
C = int(fin.readline().rstrip())
sum0 = A*2+B*3+C*4

left, right = 0, 2*A+B
while left < right:
    mid = (left+right)//2  
    sum = sum0 + mid*5
    
    if 2*sum >= 7*(A+B+C+mid):
        right = mid
    else:
        left = mid+1
        
print(left)        