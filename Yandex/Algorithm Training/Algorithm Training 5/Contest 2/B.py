from collections import deque

def get_first_profit(numbers, K):
    profit = 0

    min_val = numbers[0]
    for i in range(1, min(K, len(numbers))):
        profit = max(profit, numbers[i]-min_val)
        min_val = min(min_val, numbers[i])

    return profit

def answer(numbers, N, K):
    if len(numbers) < 2: return 0
    if K >= N: return get_first_profit(numbers, K)

    max_profit = get_first_profit(numbers, K)

    stack = deque()
    for i in range(K):
        while stack and numbers[stack[-1]] >= numbers[i]:
            stack.pop()

        stack.append(i)
 
    for i in range(K, N):       
        while stack and numbers[stack[-1]] >= numbers[i]:
            stack.pop()

        while stack and (i-stack[0] > K):
            stack.popleft()            
        
        stack.append(i)    

        max_profit = max(max_profit, numbers[i]-numbers[stack[0]])

    return max_profit


def main():
    fin = open('input.txt')

    N, K = [int(x) for x in fin.readline().split()]
    numbers = [int(x) for x in fin.readline().split()]

    print(answer(numbers, N, K))   


if __name__ == '__main__':
    main()