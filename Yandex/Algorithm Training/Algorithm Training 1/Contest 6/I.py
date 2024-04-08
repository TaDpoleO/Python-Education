fin = open('input.txt')
N, R, C = [int(x) for x in fin.readline().split()]

heights = [0]*N
for i in range(N):
    heights[i] = int(fin.readline())   
heights.sort()

# 0, ..., heights[-1]-heights[0]

def isGroupeable(diff, heights, groups_number, mans_number):
    first, groups_count = 0, 0
    while first < len(heights):
        last = min(len(heights)-1, first+mans_number-1)
        if (heights[last]-heights[first] <= diff) and (last-first+1 == mans_number):
            groups_count += 1
            first = last+1
        else:
            first += 1
    
    return groups_count >= groups_number

def bin_search(left, right, condition, cond_params):
    while left < right:
        mid = (left+right)//2        
        # FFTT, TTTT
        if condition(mid, *cond_params):
            right = mid
        else:
            left = mid+1
            
    return left
    
print(bin_search(0, heights[-1]-heights[0], isGroupeable, [heights, R, C])) 