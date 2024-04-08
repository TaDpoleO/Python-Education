inp_file = open('input.txt')
lst = [int(x) for x in inp_file.readline().split()]

def answer(lst):
    prev = lst[0]

    for x in lst[1:]:
        if prev >= x: return 'NO'
        prev = x

    return 'YES'

print(answer(lst))