from collections import defaultdict

fin = open('input.txt')
s1 = fin.readline().rstrip()
s2 = fin.readline().rstrip()

def answer(s1, s2):
    res = defaultdict(int)
    for letter in s1:
        res[letter] += 1

    for letter in s2:
        res[letter] -= 1

    for val in res.values():
        if val != 0: return 'NO'

    return 'YES'

print(answer(s1, s2))