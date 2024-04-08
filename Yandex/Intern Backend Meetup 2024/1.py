def answer(x, y, z):
    if x % 2 == y % 2 == z % 2:
        return 'No'
    else:
        return 'Yes'

def main():
    fin = open('input.txt')
    N = int(fin.readline())    
    
    result = ['']*N
    for i in range(N):
        x, y, z = [int(x) for x in fin.readline().split()]
        result[i] = answer(x, y, z)

    print('\n'.join(result))  


if __name__ == '__main__':
    main()