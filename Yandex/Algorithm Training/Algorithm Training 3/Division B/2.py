fin = open('input.txt')
K = int(fin.readline())
s = fin.readline().rstrip()

max_size = 0

for curr_letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    changes = 0
    left = right = 0
    while right < len(s):
        while (changes <= K) and right < len(s):
            if s[right] != curr_letter: changes += 1    
            right += 1            

        if right == len(s) and changes <= K: right += 1
        if right-left-1 > max_size: max_size = right-left-1

        if s[left] != curr_letter: changes -= 1
        left += 1        

print(max_size)