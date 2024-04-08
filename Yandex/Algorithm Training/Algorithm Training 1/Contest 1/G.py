inp_file = open('input.txt')
N, K, M = [int(x) for x in inp_file.readline().split()]

if (N < K) or (K < M):    
    print(0)
else:
    curr_splav, count = N, 0
    while curr_splav >= K:
        curr_zagotovka = K
        curr_splav -= K
        while curr_zagotovka >= M:
            curr_zagotovka -= M
            count += 1
        curr_splav += curr_zagotovka
        
    print(count)        