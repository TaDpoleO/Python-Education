fin = open('input.txt')
N, A, B, W, H = [int(x) for x in fin.readline().split()]

def bsearch(N, w_house, h_house, w_square, h_square):
    max_d = min(w_square, h_square)

    left, right = 0, max_d//2
    while left < right:
        mid = (left+right+1) // 2
        
        width = w_house+2*mid
        height = h_house+2*mid
        col_num = w_square // width
        row_num = h_square // height

        N_max = col_num*row_num

        if N_max >= N:
            left = mid
        else:
            right = mid-1

    return left

print(max(bsearch(N, A, B, W, H), bsearch(N, B, A, W, H)))