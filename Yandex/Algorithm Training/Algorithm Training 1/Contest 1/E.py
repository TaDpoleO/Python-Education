def get_p_and_n(K, K_on_floor, M):
    level_before = (K-1) // K_on_floor
    P_before = level_before // M

    N_before = level_before-P_before*M

    return P_before+1, N_before+1

def answer(K1, M, K2, P2, N2):
    if N2 > M:
        return -1, -1

    before_floors = (P2-1)*M+(N2-1)

    if before_floors == 0:
        if K1 <= K2:
            return 1, 1
        else:
            if M == 1:
                return 0, 1
            elif M*K2 >= K1:
                return 1, 0
            else:
                return 0, 0

    k_on_floor_v1 = (K2-1) // before_floors
    k_on_floor_v2 = K2 // (before_floors+1)
    if K2 % (before_floors+1) != 0: k_on_floor_v2 += 1

    if (k_on_floor_v1 == 0) or (k_on_floor_v2 == 0) or (k_on_floor_v2 > k_on_floor_v1):
        return -1, -1

    result = []
    for i in range(k_on_floor_v2, k_on_floor_v1+1):
        result.append(get_p_and_n(K1, i, M))

    P1, N1 = result[0]
    chech_P = check_N = True
    for Pi, Ni in result:
        if chech_P and Pi != P1:
            P1 = 0
            chech_P = False

        if check_N and Ni != N1:
            N1 = 0
            check_N = False

    return P1, N1

def main():
    with open('input.txt') as fin:
        K1, M, K2, P2, N2 = [int(x) for x in fin.readline().split()]

        print(*answer(K1, M, K2, P2, N2))


if __name__ == '__main__':
    main()