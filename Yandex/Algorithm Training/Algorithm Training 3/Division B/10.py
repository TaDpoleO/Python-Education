from collections import defaultdict

fin = open('input.txt')
s = fin.readline().rstrip()

letters = [0]*len(s)
for i in range(len(s)):
    letters[i] = (i+1)*(len(s)-i)
    
letter_count = defaultdict(int)
for i, letter in enumerate(s):
    letter_count[letter] += letters[i]
    
for key in sorted(letter_count.keys()):
    print(f'{key}: {letter_count[key]}')