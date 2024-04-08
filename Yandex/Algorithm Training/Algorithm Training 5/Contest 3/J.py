from collections import defaultdict

def get_next_part(dev, downloaded, finished):
    for _, next_part in downloaded:
        if next_part not in finished[dev]: return next_part
        
def get_next_source(part, finished):
    sources = []

    for i in range(len(finished)):
        if part in finished[i]: sources.append((i, len(finished[i])))

    min_finished = next_source = float('inf')
    for source, count in sources:
        if count < min_finished:
            min_finished = count
            next_source = source
        elif count == min_finished:
            if source < next_source: next_source = source

    return next_source

def get_next_worth_request(cur_dev, requests, worth, finished):
    if not requests: return None, None

    max_worth = float('-inf')
    for dev, _ in requests:
        if worth[cur_dev][dev] > max_worth:
            max_worth = worth[cur_dev][dev]

    min_finished = next_dev = float('inf')
    for dev, _ in requests:
        if worth[cur_dev][dev] == max_worth:            
            if len(finished[dev]) < min_finished:
                min_finished = len(finished[dev])
                next_dev = dev
            elif len(finished[dev]) == min_finished:
                if dev < next_dev: next_dev = dev

    for dev, part in requests:
        if dev == next_dev:
            return dev, part

def answer(N, K):
    timing = [0]*N

    finished = [set() for _ in range(N)]
    finished[0] = set(list(range(K)))

    downloaded_parts = [(1, x) for x in range(K)]

    worth = [[0]*N for _ in range(N)]
    for i in range(N):
        worth[i][i] = -1
    
    cur_time = 1
    while sum([len(x) for x in finished]) < N*K:
        requests = defaultdict(list)
        completed_requests = []

        for cur_dev in range(1, N):
            if len(finished[cur_dev]) < K:
                next_part = get_next_part(cur_dev, downloaded_parts, finished)
                next_source = get_next_source(next_part, finished)
                requests[next_source].append((cur_dev, next_part))

        for cur_dev in range(N):
            next_dev, next_part = get_next_worth_request(cur_dev, requests[cur_dev], worth, finished)

            if next_dev is not None:
                completed_requests.append((cur_dev, next_dev, next_part))

        for cur_dev, next_dev, next_part in completed_requests:
            finished[next_dev].add(next_part)
            if len(finished[next_dev]) == K:
                timing[next_dev] = cur_time

            for i in range(K):
                if downloaded_parts[i][1] == next_part:
                    downloaded_parts[i] = (downloaded_parts[i][0]+1, downloaded_parts[i][1])

            worth[next_dev][cur_dev] += 1
        
        downloaded_parts.sort()
        cur_time += 1
    
    return ' '.join([str(x) for x in timing[1:]])

def main():
    with open('input.txt') as fin:
        N, K = [int(x) for x in fin.readline().split()]
        print(answer(N, K))


if __name__ == '__main__':    
    main()