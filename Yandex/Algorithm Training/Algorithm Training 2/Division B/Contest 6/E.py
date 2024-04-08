def countK(array, L):
    count = 1

    end_num = array[0]+L
    for i in range(len(array)):
        if array[i] > end_num:
            count += 1
            end_num = array[i]+L

    return count

def bsearch_length(array, left, right, K):
    while left < right:
        mid = (left+right)//2
        # FFTT, TTTT
        if countK(array, mid) <= K:            
            right = mid
        else:
            left = mid+1

    return left


if __name__ == '__main__':
    fin = open('input.txt')
    N, K = [int(x) for x in fin.readline().split()]
    numbers = [int(x) for x in fin.readline().split()]
    numbers.sort()

    print(bsearch_length(numbers, 0, numbers[-1]-numbers[0], K))