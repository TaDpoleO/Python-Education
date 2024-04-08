from collections import defaultdict

fin = open('input.txt')
n, k = [int(x) for x in fin.readline().split()]
cards = defaultdict(int)
for x in fin.readline().split():
    cards[int(x)] += 1
cards_set = list(sorted(cards.keys()))

count = 0
curr_twice_nums = 0
left = right = 0
while left < len(cards_set):
    if cards[cards_set[left]] >= 2: curr_twice_nums -= 1

    while right < len(cards_set) and cards_set[left]*k >= cards_set[right]:
        if cards[cards_set[right]] >= 2: curr_twice_nums += 1
        right += 1

    if cards[cards_set[left]] >= 3: count += 1
    if cards[cards_set[left]] >= 2: count += ((right-1)-left)*3        
    count += ((right-1)-left)*((right-1)-left-1)*3
    count += curr_twice_nums*3

    left += 1

print(count)