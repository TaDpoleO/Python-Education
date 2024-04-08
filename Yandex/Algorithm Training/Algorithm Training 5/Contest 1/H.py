def answer(L, x1, v1, x2, v2):
    if min(x1, L-x1) == min(x2, L-x2): return 0
    if v1 == v2 == 0: return None

    if v1 != v2:
        t1 = (x2-x1)/(v1-v2)
        T1 = abs(L/(v1-v2))
        t1 -= (t1//T1)*T1
    else:
        t1 = float('inf')  

    if v1 != -v2:
        t2 = -(x2+x1)/(v1+v2)
        T2 = abs(L/(v1+v2))
        t2 -= (t2//T2)*T2
    else:
        t2 = float('inf')  

    t = min(t1, t2)
    
    return t

def main():
    with open('input.txt') as fin:         
        L, x1, v1, x2, v2 = [int(x) for x in fin.readline().split()]
        result = answer(L, x1, v1, x2, v2)
        if result is not None:
            print('YES')
            print(f'{result:.10f}')
        else:
            print('NO')


if __name__ == '__main__':
    main()