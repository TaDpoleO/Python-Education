from collections import defaultdict

fin = open('input.txt')
letters = defaultdict(int)

max_letters = 0
for line in fin:
    for letter in line.rstrip():
        if letter != ' ':
            letters[letter] += 1        
            max_letters = max(max_letters, letters[letter])

letter_order = sorted(letters, key=lambda x: ord(x))

for i in range(max_letters):
    line = []
    for letter in letter_order:
        if max_letters-letters[letter] <= i:
            line.append('#')
        else:
            line.append(' ')
    print(''.join(line))
print(''.join(letter_order))