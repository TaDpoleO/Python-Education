def compactTreeToTree(compact_tree):
    root = ['', None, None, None] # val, left, right, up

    res = []    
    curr_node, curr_code = root, []
    for ch in compact_tree:
        if ch == 'D':
            if curr_node[1] is None:
                curr_node[1] = ['0', None, None, curr_node]
                curr_node = curr_node[1]
                curr_code.append('0')
            elif curr_node[2] is None:
                curr_node[2] = ['1', None, None, curr_node]
                curr_node = curr_node[2]
                curr_code.append('1')
        elif ch == 'U':
            res.append(''.join(curr_code))            

            while curr_node[0] == '1':
                curr_node = curr_node[3]
                curr_code.pop()

            if curr_node[0] == '0':
                curr_node = curr_node[3]
                curr_node[2] = ['1', None, None, curr_node]
                curr_node = curr_node[2]
                curr_code.pop()
                curr_code.append('1')
    
    res.append(''.join(curr_code))
    return res

fin = open('input.txt')
N = int(fin.readline())

trees = [0]*N
for i in range(N):
    trees[i] = fin.readline().rstrip()
    ans = compactTreeToTree(trees[i])
    print(len(ans))
    print('\n'.join(ans))