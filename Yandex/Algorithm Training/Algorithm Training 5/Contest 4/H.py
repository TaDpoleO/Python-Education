def get_prefix_sum(prefix, l, r):
    return prefix[r+1]-prefix[l]

def get_votes(parties, min_party, other_max_votes):
    N = len(parties)

    votes = [votes for votes, _, _ in parties]
    
    buy_from = set()
    bought_votes = 0    

    for i in range(N):
        if (i != min_party) and (votes[i] > other_max_votes):
            bought_votes += votes[i]-other_max_votes
            votes[i] = other_max_votes
            buy_from.add(i)

    votes[min_party] += bought_votes


    for cur_party in buy_from:
        if (bought_votes > 0) and votes[min_party]-other_max_votes > 2:
            votes[cur_party] += 1
            bought_votes -= 1
            votes[min_party] -= 1            
        else:
            break

    res_votes = [0]*N
    for i in range(N):
        res_votes[parties[i][2]] = votes[i]

    return res_votes

def get_fst_index_of_big_party(parties, left, right, max_other_votes):
    while left < right:
        mid = (left+right)//2

        # FFTT, TTTT
        if parties[mid][0] >= max_other_votes:
            right = mid
        else:
            left = mid+1

    return left

def isWinnable(parties, prefix, cur_party, max_other_votes):
    N = len(parties)
   
    index = get_fst_index_of_big_party(parties, 0, N-1, max_other_votes)
    delta_votes = get_prefix_sum(prefix, index, N-1)-(N-index)*max_other_votes

    if cur_party >= index:
        delta_votes -= parties[cur_party][0]-max_other_votes

    if parties[cur_party][0]+delta_votes > max_other_votes:
        cur_delta = parties[cur_party][0]+delta_votes-max_other_votes
        if cur_delta > 2:
            can_reduce = cur_delta-2

            if delta_votes > can_reduce:
                delta_votes -= can_reduce
            else:
                delta_votes = 0

        return delta_votes+parties[cur_party][1]
    else:
        return False

def get_min_money_and_other_votes(parties, prefix, cur_party, max_votes):
    left = 0
    right = max_votes

    money = isWinnable(parties, prefix, cur_party, 0)
    
    while left < right:
        mid = (left+right+1)//2
       
        # TTFF, TTTT
        if (res := isWinnable(parties, prefix, cur_party, mid)):
            money = res
            left = mid
        else:
            right = mid-1

    return money, left

def answer(parties, prefix):
    N = len(parties)

    max_votes = max([votes for votes, _, _ in parties])

    min_money, min_other_votes, min_party = float('inf'), float('inf'), 0
    for i in range(N):
        if parties[i][1] != -1:
            cur_money, cur_other_votes = get_min_money_and_other_votes(parties, prefix, i, max_votes)
            if cur_money < min_money:
                min_money = cur_money
                min_other_votes = cur_other_votes
                min_party = i

    votes = get_votes(parties, min_party, min_other_votes)
    
    return min_money, parties[min_party][2]+1, votes

def main():
    with open('input.txt') as fin:
        N = int(fin.readline())
        parties = [(0, 0)]*N

        for i in range(N):
            parties[i] = tuple([int(x) for x in fin.readline().split()]+[i])
        parties.sort()

        prefix = [0]*(N+1)
        for i in range(N):
            prefix[i+1] = prefix[i]+parties[i][0]

        money, party, votes = answer(parties, prefix)
        
        with open('output.txt', 'w') as fout:
            fout.write(f'{money}\n')
            fout.write(f'{party}\n')
            fout.write(f'{" ".join([str(x) for x in votes])}\n')


if __name__ == '__main__':
    main()