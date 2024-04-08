inp_file = open('input.txt')

N = int(inp_file.readline())

res_dict = dict()
for _ in range(N):
    w1, w2 = inp_file.readline().split()
    res_dict[w1] = w2
    res_dict[w2] = w1
    
word = inp_file.readline().rstrip()
print(res_dict[word])