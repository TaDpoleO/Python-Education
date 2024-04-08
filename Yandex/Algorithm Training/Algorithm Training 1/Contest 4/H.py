def getIndex(ch):
    return ord(ch)-65 if ord(ch) <= 90 else ord(ch)-71

fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]

g = fin.readline().rstrip()
S = fin.readline().rstrip()

word = [0]*52
for ch in g:
    word[getIndex(ch)] += 1

word_count, curr_word = 0, [0]*52
left = right = 0
while right < M:
    curr_letter = S[right]

    if word[getIndex(curr_letter)] > 0:
        curr_word[getIndex(curr_letter)] += 1

        while curr_word[getIndex(curr_letter)] > word[getIndex(curr_letter)]:
            curr_word[getIndex(S[left])] -= 1
            left += 1

        if right-left+1 == len(g):
            word_count += 1
            curr_word[getIndex(S[left])] -= 1
            left += 1
    else:
        curr_word = [0]*52
        left = right+1

    right += 1

print(word_count)
