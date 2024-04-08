def answer(N, W, L, blocks):
    EVENT_BLOCK_START = 20
    EVENT_BLOCK_END = 10

    events = [(0, 0, 0)]*2*N
    for i in range(N):
        x1, y1, z1, x2, y2, z2 = blocks[i]
        S = abs(x2-x1)*abs(y2-y1)
        events[2*i] = (z1, EVENT_BLOCK_START, S)
        events[2*i+1] = (z2, EVENT_BLOCK_END, S)
    events.sort()

    res_z, res_len = float('inf'), float('inf')
    target_S, cur_S, cur_blocks = W*L, 0, 0
    for event in events:
        z, event_type, S = event

        if event_type == EVENT_BLOCK_START:
            cur_blocks += 1
            cur_S += S
            if cur_S == target_S:
                if cur_blocks < res_len:
                    res_z = z
                    res_len = cur_blocks

        elif event_type == EVENT_BLOCK_END:
            cur_blocks -= 1
            cur_S -= S

    result = []
    for i in range(N):
        x1, y1, z1, x2, y2, z2 = blocks[i]

        if z1 <= res_z and res_z < z2:
            result.append(i+1)

    return result

def main():
    with open('input.txt') as fin:
        N, W, L = [int(x) for x in fin.readline().split()]

        blocks = [(0, 0, 0, 0, 0, 0)]*N
        for i in range(N):
            blocks[i] = tuple([int(x) for x in fin.readline().split()])

        res = answer(N, W, L, blocks)
        if res:
            print('YES')
            print(len(res))
            print(' '.join([str(x) for x in res]))
        else:
            print('NO')


if __name__ == '__main__':
    main()