from collections import defaultdict

def getAccentNumber(word):
    count = 0
    for ch in word:
        if not ch.islower(): count += 1

    return count

inp_file = open('input.txt')

N = int(inp_file.readline())
dictionary = defaultdict(set)

for _ in range(N):
    word = inp_file.readline().rstrip()
    dictionary[word.lower()].add(word)

errors = 0
for word in inp_file.readline().split():
    key = word.lower()
    if (key in dictionary):
        if word not in dictionary[key]: errors += 1
    else:
        if getAccentNumber(word) != 1:
            errors += 1
print(errors)