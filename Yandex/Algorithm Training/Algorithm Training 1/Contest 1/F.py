inp_file = open('input.txt')

a1, b1, a2, b2 = [int(x) for x in inp_file.readline().rstrip().split()]

S1 = (a1+a2)*max(b1, b2)
S2 = (a1+b2)*max(b1, a2)
S3 = (b1+a2)*max(a1, b2)
S4 = (b1+b2)*max(a1, a2)

res_a, res_b, curr_S = a1+a2, max(b1, b2), S1
if S2 < curr_S:
    res_a, res_b, curr_S = a1+b2, max(b1, a2), S2
if S3 < curr_S:
    res_a, res_b, curr_S = b1+a2, max(a1, b2), S3
if S4 < curr_S:
    res_a, res_b, curr_S = b1+b2, max(a1, a2), S4

print(res_a, res_b)