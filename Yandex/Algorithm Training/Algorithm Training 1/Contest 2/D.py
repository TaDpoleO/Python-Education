inp_file = open('input.txt')
array = [int(x) for x in inp_file.readline().split()]

def answer(array):
    if len(array)<3: return 0
            
    count = 0
    for i in range(1,len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            count += 1
    
    return count
    
print(answer(array))