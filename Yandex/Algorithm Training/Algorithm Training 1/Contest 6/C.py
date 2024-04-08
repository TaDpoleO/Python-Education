fin = open('input.txt')

W, H, N = [int(x) for x in fin.readline().split()]

def getReqiuredHeight(w_num, width, height, number):
    rows = number // w_num
    if number % w_num != 0: rows += 1
    
    square_height = rows*height
    return square_height <= width*w_num

left, right = 1, N
while left < right:
    mid = (left+right) // 2
    if getReqiuredHeight(mid, W, H, N):
        right = mid
    else:
        left = mid+1
left0 = left

left, right = 1, N
while left < right:
    mid = (left+right) // 2
    if getReqiuredHeight(mid, H, W, N):
        right = mid
    else:
        left = mid+1
left1 = left

print(min(left0*W, left1*H))