inp_file = open('input.txt')
array = [int(x) for x in inp_file.readline().split()]

def answer(array):
    temp_slice = sorted(array[:3])
    max3, max2, max1 = temp_slice
    min1, min2 = temp_slice[0], temp_slice[1]

    for num in array[3:]:
        if num > max1:
            max1, max2, max3 = num, max1, max2
        elif num > max2:
            max2, max3 = num, max2
        elif num > max3:
            max3 = num
        
        if num < min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num
            
    if (min1 >= 0) or (max1 < 0):
        return max3, max2, max1
    elif (max2 < 0) or (max3 < 0):
        return min1, min2, max1
    elif max3 >= 0:
       if max1*max2*max3 > min1*min2*max1:
           return max3, max2, max1
       else:
           return min1, min2, max1

print(*answer(array))