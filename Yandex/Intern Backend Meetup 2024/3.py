def hasMaxVal(left, right, max_prefix):
    return (max_prefix[right+1]-max_prefix[left]) > 0

def hasMinVal(left, right, min_prefix):
    return (min_prefix[right+1]-min_prefix[left]) > 0

def hasMaxReaction(left, right, max_prefix, min_prefix):
    return hasMaxVal(left, right, max_prefix) and hasMinVal(left, right, min_prefix)

def get_first_index(size, N, max_prefix, min_prefix):
    for i in range(N-size+1):
        if hasMaxReaction(i, i+size-1, max_prefix, min_prefix):
            return i

    return None

def bsearch(left, right, max_prefix, min_prefix):
    N = right

    index = None
    last_succes = None, None

    while left < right:
        mid = (left+right)//2

        # FFTT
        index = get_first_index(mid, N, max_prefix, min_prefix)
        if index is not None:
            right = mid
            last_succes = mid, index
        else:
            left = mid+1
    
    if index is None:
        if last_succes[1] is None:
            return N, 0
        else:
            return last_succes
    else:
        return left, index
    
def main():
    fin = open('input.txt')
    emotional_stream = fin.readline().rstrip()

    N = len(emotional_stream)
    
    if N < 2:
        print(emotional_stream)
        return

    reactions = [ord(x) for x in emotional_stream]
    
    max_val = max(reactions)
    min_val = min(reactions)

    max_prefix = [0]*(N+1)
    for i in range(N):
        if reactions[i] == max_val:
            max_prefix[i+1] = max_prefix[i]+1
        else:
            max_prefix[i+1] = max_prefix[i]

    min_prefix = [0]*(N+1)
    for i in range(N):
        if reactions[i] == min_val:
            min_prefix[i+1] = min_prefix[i]+1
        else:
            min_prefix[i+1] = min_prefix[i]
       
    size, index = bsearch(1, N, max_prefix, min_prefix)
    print(emotional_stream[index:index+size])
    

if __name__ == '__main__':
    main()