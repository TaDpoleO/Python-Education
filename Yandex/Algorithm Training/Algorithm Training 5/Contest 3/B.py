from io import TextIOWrapper
from collections import defaultdict

def answer(fin: TextIOWrapper):
    result = defaultdict(int)

    for ch in fin.readline().rstrip():
        result[ch] += 1

    for ch in fin.readline().rstrip():
        result[ch] -= 1

    for val in result.values():
        if val != 0:
            return 'NO'
    
    return 'YES'   

def main():
    with open('input.txt') as fin:
        print(answer(fin))


if __name__ == '__main__':
    main()