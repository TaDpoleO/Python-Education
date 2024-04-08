import re
from collections import OrderedDict

def hasAlpha(word):
    for ch in word:
        if ch.isalpha() or ch == '_': return True
    return False

inp_file = open('input.txt')

N, C, D = inp_file.readline().split()
N = int(N)
FLAG_CASE_SENS = True if C == 'yes' else False
FLAG_START_0 = True if D == 'yes' else False

keywords = set()
for _ in range(N):
    word = inp_file.readline().rstrip()
    if not FLAG_CASE_SENS: word = word.lower()
    keywords.add(word)    

id_dict, max_count = OrderedDict(), 0
for line in inp_file:
    for word in re.findall('(\w+)', line):
    	if (FLAG_START_0) or not word[0].isnumeric():
            if not FLAG_CASE_SENS: word = word.lower()
            if (word not in keywords) and hasAlpha(word):
                id_dict[word] = id_dict.get(word, 0)+1
                max_count = max(id_dict[word], max_count)

for key in id_dict.keys():
    if id_dict[key] == max_count:
        print(key)
        break