import sys
from collections import defaultdict

def answer(letters):
    word = {'T': 1, 'I': 1, 'N': 1, 'K': 1, 'O': 1, 'F': 2}
    word_length = 7

    if len(letters) != word_length: return False

    curr_word = defaultdict(int)
    for ch in letters:
        curr_word[ch] += 1
        if (ch not in word) or curr_word[ch] > word[ch]: return False

    return True

# fin = open('input.txt')
fin = sys.stdin

T = int(fin.readline())
for _ in range(T):
    letters = fin.readline().rstrip()
    if answer(letters):
        print('Yes')
    else:
        print('No')