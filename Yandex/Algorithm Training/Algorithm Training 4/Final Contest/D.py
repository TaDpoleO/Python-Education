def answer(array, length):
    def permute(size_of_bricks, used_bricks, curr_index, curr_length, need_length, curr_result, result, remain_sum):
        if curr_length == need_length:
            if len(curr_result) < len(result): result[:] = curr_result.copy()
            return
        elif curr_length < need_length and curr_length+remain_sum >= need_length and curr_index < len(used_bricks):
            if  used_bricks[curr_index] < 2:
                used_bricks[curr_index] += 1
                curr_length += size_of_bricks[curr_index]
                curr_result.append(size_of_bricks[curr_index])

                permute(size_of_bricks, used_bricks, curr_index, curr_length, need_length, curr_result, result, remain_sum-size_of_bricks[curr_index])

                used_bricks[curr_index] -= 1
                curr_length -= size_of_bricks[curr_index]
                curr_result.pop()

                curr_index += 1
                permute(size_of_bricks, used_bricks, curr_index, curr_length, need_length, curr_result, result, remain_sum-size_of_bricks[curr_index-1]*(2-used_bricks[curr_index-1]))
            else:
                curr_index += 1
                permute(size_of_bricks, used_bricks, curr_index, curr_length, need_length, curr_result, result, remain_sum)

    max_length = sum(array)*2

    if max_length < length:
        return -1, []
    elif max_length == length:
        res = array*2
        return len(res), res
    
    used_bricks = [0]*len(array)
    curr_result, result = [], [0]*(len(array)*2+1)

    permute(array, used_bricks, 0, 0, length, curr_result, result, max_length)
  
    if len(result) != len(array)*2+1:
        return len(result), result
    else:
        return 0, []

fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]
array = [int(x) for x in fin.readline().split()]
array.sort(reverse=True)

res, bricks = answer(array, N)
if res == 0:
    print(0)
elif res == -1:
    print(-1)
else:
    print(res)
    print(*bricks)