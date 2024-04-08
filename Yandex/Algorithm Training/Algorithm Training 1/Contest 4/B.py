inp_file = open('input.txt')
from collections import defaultdict

word_counter = defaultdict(int)
for line in inp_file:
    for word in line.split():
        print(word_counter[word], end=' ')
        word_counter[word] += 1