fin = open('input.txt')
K = int(fin.readline())
s = fin.readline().rstrip()

count, in_count = 0, False
curr_template, curr_index = s[:K], 0
left, right = 0, K-1

while right+1 < len(s):
    if s[right+1] == curr_template[curr_index]:
        in_count = True
        right += 1
        curr_index = (curr_index+1) % K
    else:
        if in_count:
            count += (right+1-left-K+1)*(right+1-left-K)//2                     
        left = right+2-K
        right = right+1
        
        curr_template = s[left:right+1]
        in_count = False
        curr_index = 0
  
if in_count:
    count += (right+1-left-K+1)*(right+1-left-K)//2

print(count)