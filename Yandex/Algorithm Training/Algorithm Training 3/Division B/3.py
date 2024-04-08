fin = open('input.txt')
N = int(fin.readline())

stickers = set([int(x) for x in fin.readline().split()])
stickers = sorted(stickers)

def bsearch(array, left, right, val):
    while left < right:
        mid = (left+right)//2
        # TTTT, FFFF, TTFF, search for first F
        if array[mid] < val:
            left = mid+1
        else:
            right = mid

    if left == len(array)-1 and array[left] < val: left += 1
    return left

K = int(fin.readline())
answers = [None]*K
for i, num in enumerate([int(x) for x in fin.readline().split()]):
    answers[i] = str(bsearch(stickers, 0, len(stickers)-1, num))

print('\n'.join(answers))