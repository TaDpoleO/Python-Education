from collections import defaultdict

fin = open('input.txt')
words = defaultdict(int)

for line in fin:
    for word in line.split():
        words[word] += 1

for word in sorted(words, key=lambda x: (-words[x], x)):
    print(word)