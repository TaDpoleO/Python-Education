fin = open('input.txt')
s = fin.readline().rstrip()

def countDiff(s):
    mod_s = ['#']

    for ch in s:
        mod_s.append(ch)
        mod_s.append('#')

    center_index = len(mod_s)//2

    diff = 0
    for i in range((len(mod_s)-1)//2):
        if mod_s[center_index+i] != mod_s[center_index-i]: diff += 1

    return diff

print(countDiff(s))