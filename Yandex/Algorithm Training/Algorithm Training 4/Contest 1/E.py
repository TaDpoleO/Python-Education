fin = open('input.txt')
N = int(fin.readline())
array = [fin.readline().rstrip() for _ in range(N)]
M = len(array[0])

print('Initial array:')
print(', '.join(array))
print('**********')

phase = 1
while phase <= M:
    print(f'Phase {phase}')
    buffer = [0]*N
    bucket = [0]*10
    bucket_for_print = [[] for _ in range(10)]
    bucket_indices = [0]*10

    for num in array:
        bucket[int(num[M-phase])] += 1

    for i in range(1, 10):
        bucket_indices[i] = bucket[i-1]+bucket_indices[i-1]

    for num in array:
        buffer[bucket_indices[int(num[M-phase])]] = num
        bucket_indices[int(num[M-phase])] += 1
        bucket_for_print[int(num[M-phase])].append(num)

    # print
    for i in range(10):
        if bucket_for_print[i] == []: bucket_for_print[i] = ['empty']

    for i in range(10):
        print(f'Bucket {i}: {", ".join(bucket_for_print[i])}')
    # end of print  

    array[:] = buffer    
    phase += 1
    print('**********')


print('Sorted array:')
print(', '.join(array))

