from collections import defaultdict
inp_file = open('input.txt')

word_counter, max_count, max_word = defaultdict(int), 0, ''
for line in inp_file:
    for word in line.split():
        word_counter[word] += 1        
        if word_counter[word] > max_count:
            max_count = word_counter[word]
            max_word = word
        elif word_counter[word] == max_count:
            if word < max_word: max_word = word
            
print(max_word)