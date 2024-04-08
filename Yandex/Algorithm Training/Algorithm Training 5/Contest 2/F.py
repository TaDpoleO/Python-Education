def rotation(array, min_sector, max_sector):
    N = len(array)
    profit = float('-inf')
 
    cur_step, steps = 0, (max_sector-min_sector+1) % N
    cur_sector = min_sector
    while cur_step < steps:
        profit = max(profit, array[cur_sector])
        cur_sector = (cur_sector+1) % N
        cur_step += 1

    return profit

def answer(numbers, A, B, K):
    N = len(numbers)

    min_steps = (A-1) // K
    max_steps = (B-1) // K

    total_sectors = max_steps-min_steps+1
    if total_sectors >= N: return max(numbers)

    min_sector = min_steps % N
    max_sector = max_steps % N

    max_profit1 = rotation(numbers, min_sector, max_sector)
    max_profit2 = rotation(numbers, (-max_sector) % N, (-min_sector) % N)

    return max(max_profit1, max_profit2)
       
def main():
    with open('input.txt') as fin:         
        N = int(fin.readline())
        numbers = [int(x) for x in fin.readline().split()]
        A, B, K = [int(x) for x in fin.readline().split()]

        print(answer(numbers, A, B, K))


if __name__ == '__main__':
    main()