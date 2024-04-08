fin = open('input.txt')
N = int(fin.readline())
M = int(fin.readline())
num = int(fin.readline())

def canBuild(width, N, M, total_num):
    total = 2*width*(N+M-2*width)
    
    return total <= total_num
    
def bin_search(left, right, condition, cond_param):
    while left < right:
        mid = (left+right+1)//2
        
        # TTTTFFFF
        if condition(mid, *cond_param):
            left = mid            
        else:
            right = mid-1
            
    return left

# 0, 1, 2, 3, ..., min(N, M)//2    
print(bin_search(0, min(N, M)//2, canBuild, [N, M, num]))