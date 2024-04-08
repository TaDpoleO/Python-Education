def getBalloonsNumber(T, Z, Y, work_time):    
    period = Z*T+Y

    period_num = work_time // period
    if period_num == 0:
        if work_time >= Z*T:
            return Z
        else:
            return work_time // T
    else:
        period_balloons = period_num*Z
        remain_time = work_time-period_num*period

        if remain_time >= Z*T:
            return period_balloons+Z
        else:
            return period_balloons+(remain_time // T)

def getBalloonsTime(T, Z, Y, count):
    period = Z*T+Y

    period_num = count // Z

    if period_num*Z == count:
        return period_num*period-Y
    else:    
        return period_num*period + (count-period_num*Z)*T
    
def check(work_time, *check_param):
    workers, balloons_need = check_param

    balloons_num = 0
    for i in range(len(workers)):
        balloons_num += getBalloonsNumber(*workers[i], work_time)

    return balloons_num >= balloons_need

def b_search(left, right, check, check_param):
    while left < right:
        mid = (left+right)//2

        # FFTT, TTTT
        if check(mid, *check_param):
            right = mid
        else:
            left = mid+1

    return left

def answer(M, N, workers):
    if M == 0: return 0, [0]*N

    max_time = float('inf')
    for i in range(N):
        curr_max_time = getBalloonsTime(*workers[i], M)
        if curr_max_time < max_time: max_time = curr_max_time

    work_time = b_search(1, max_time, check, [workers, M])
    balloons_per_worker = [0]*N
    for i in range(N):
        balloons_per_worker[i] = getBalloonsNumber(*workers[i], work_time)

    return work_time, balloons_per_worker

fin = open('input.txt')
M, N  = [int(x) for x in fin.readline().split()]

workers = [(0, 0, 0)]*N
for i in range(N):
    workers[i] = tuple([int(x) for x in fin.readline().split()])

ans = answer(M, N, workers)
balloons = sum(ans[1])

if balloons > M:
    surplus = balloons-M    
    i = 0
    while surplus > 0:
        ans[1][i] -= 1
        i += 1
        surplus -= 1

print(ans[0])
print(*ans[1])