inp_file = open('input.txt')
array = [int(x) for x in inp_file.readline().rstrip().split()]

plus1, plus2 = max(array[0], array[1]), min(array[0], array[1])
minus1, minus2 = plus2, plus1

for num in array[2:]:
    if num > plus1:
        plus1, plus2 = num, plus1
    elif num > plus2:
        plus2 = num

    if num < minus1:
        minus1, minus2 = num, minus1
    elif num < minus2:
        minus2 = num
              
if plus1*plus2 > minus1*minus2:
    print(plus2, plus1)
else:
    print(minus1, minus2)