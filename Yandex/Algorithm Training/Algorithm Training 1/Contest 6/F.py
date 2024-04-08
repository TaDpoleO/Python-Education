fin = open('input.txt')
N, t1, t2 = [int(x) for x in fin.readline().split()]

def isSucces(time, t1, t2, N):
    if N == 0: return True
    
    time -= min(t1, t2)    
    if time < 0: return False
    N1 = time // t1
    N2 = time // t2
    
    return N1+N2+1 >= N
   
def bsearch(left, right, condition, cond_params):
    while left < right:
        mid = (left+right)//2
        
        # FFFFTTTT >> first T
        if condition(mid, *cond_params):
            right = mid
        else:
            left = mid + 1
            
    return left

left, right = 0, min(t1, t2)*N
print(bsearch(left, right, isSucces, [t1, t2, N]))