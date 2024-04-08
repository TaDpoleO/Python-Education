def findMedianSortedArrays(nums1, nums2) -> float:
    def findInsertIndex(nums, val):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            # FFFF, TTTT, TTFF
            if nums[mid] < val:
                left = mid+1
            else:
                right = mid
        
        if left == len(nums)-1 and nums[left] < val: left += 1
        return left       
    
    def findMedian(nums1, nums2, left, right):
        l, r = left, right
        while l < r:                
            mid = (l+r+1)//2
            # TTFF >> search for last T
            index1 = findInsertIndex(nums1, mid)
            index2 = findInsertIndex(nums2, mid)

            if index1+index2 < len(nums1)-index1+len(nums2)-index2:
                l = mid
            else:
                r = mid-1

        return l
    
    return findMedian(nums1, nums2, min(nums1[0], nums2[0]), max(nums1[-1], nums2[-1]))

def genArray(array, x1, d1, a, c, m):
    next_x, prev_d = x1, d1
    for i in range(len(array)):
        array[i] = next_x
        next_x = next_x+prev_d
        prev_d = (a*prev_d+c) % m

fin = open('input.txt')
N, L = [int(x) for x in fin.readline().split()]

arrays = [[0]*L for _ in range(N)]
for i in range(N):
    genArray(arrays[i], *[int(x) for x in fin.readline().split()])

for i in range(N):
    arrI = arrays[i]

    for j in range(i+1, N): 
        arrJ = arrays[j]
        median = findMedianSortedArrays(arrI, arrJ)
        print(median)