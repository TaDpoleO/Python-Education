def answer(N, K, D):
    next_val = ((N*10) // K)*K

    if next_val < N*10:
        next_val += K

    if next_val > (N*10+9):
        return -1
    
    return str(next_val)+'0'*(D-1)

def main():
    fin = open('input.txt')
    N, K, D = [int(x) for x in fin.readline().split()]
    print(answer(N, K, D))


if __name__ == '__main__':
    main()