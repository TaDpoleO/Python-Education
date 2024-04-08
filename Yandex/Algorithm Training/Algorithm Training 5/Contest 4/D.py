def get_rows(words, width):
    rows = 1
    cur_letters = words[0]

    for i in range(1, len(words)):
        if cur_letters+1+words[i] <= width:
            cur_letters = cur_letters+1+words[i]
        else:
            cur_letters = words[i]
            rows += 1

    return rows

def answer(words1, words2, width, left, right):
    left_border = left

    while left < right:
        mid = (left+right)//2

        left_rows = get_rows(words1, mid)
        right_rows = get_rows(words2, width-mid)

        # FFTT, TTTT
        if left_rows <= right_rows:
            right = mid
        else:
            left = mid+1

    min_rows1 = max(get_rows(words1, left), get_rows(words2, width-left))
    if left > left_border:
        min_rows2 = max(get_rows(words1, left-1), get_rows(words2, width-left+1))
    else:
        min_rows2 = float('inf')

    return min(min_rows1, min_rows2)

def main():
    with open('input.txt') as fin:
        W, _, _ = [int(x) for x in fin.readline().split()]
        words1 = [int(x) for x in fin.readline().split()]
        words2 = [int(x) for x in fin.readline().split()]

        min_left_w = max(words1)
        min_right_w = max(words2)

        print(answer(words1, words2, W, min_left_w, W-min_right_w))


if __name__ == '__main__':
    main()