def main():
    fin = open('input.txt')
    K = int(fin.readline())
    
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')

    for _ in range(K):
        x, y = [int(x) for x in fin.readline().split()]

        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(min_x, min_y, max_x, max_y)

if __name__ == '__main__':
    main()