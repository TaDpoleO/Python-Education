from collections import defaultdict

fin = open('input.txt')
N, K = [int(x) for x in fin.readline().split()]
s = fin.readline().rstrip()

curr_dict, left, max_length, max_length_index = defaultdict(int), 0, 1, 0
curr_dict[s[0]] = 1

for i in range(1,N):
   curr_dict[s[i]] += 1

   while curr_dict[s[i]] > K:
       curr_dict[s[left]] -= 1
       left += 1
   
   if i-left+1 > max_length:
       max_length = i-left+1
       max_length_index = left

print(max_length, max_length_index+1)