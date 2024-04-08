import math

def isPrime(number, prev_primes=None):
    if number == 2: return True
    if number % 2 == 0: return False

    if prev_primes is not None:
        check_range = prev_primes
    else:
        start_num = 3
        end_num = int(math.sqrt(number))

        check_range = range(start_num, end_num+1, 2)

    for num in check_range:
        if number % num == 0: return False

    return True

def getPrimes(max_number):
    if max_number == 2: return [2]
    res = [2]

    for num in range(3, max_number, 2):
        if isPrime(num, res): res.append(num) 

    return res

if __name__ == '__main__':
    import time
    time0 = time.time()

    N = 10**4
    prime_numbers = getPrimes(N)
    print(prime_numbers)
    print(time.time()-time0)

    fin = open('input.txt')
    temp = []
    for line in fin:
        temp.extend([int(x) for x in line.split()])

    trigger = True
    for i in range(min(len(prime_numbers), len(temp))):
        if prime_numbers[i] != temp[i]: trigger = False
    print(f'Check: {trigger}')

    print(f'1073676287 is Prime: {isPrime(1073676287)}')