from collections import defaultdict

fin = open('input.txt')

N = int(fin.readline())
classes = [int(x) for x in fin.readline().split()]
# classes.sort()

M = int(fin.readline())
cond_bases = defaultdict(lambda: 1001)
for _ in range(M):
    power, cost = [int(x) for x in fin.readline().split()]
    cond_bases[power] = min(cond_bases[power], cost)
    
powers = sorted(cond_bases.keys())
min_cost = cond_bases[powers[-1]]
for i in range(len(powers)-1, -1, -1):
   min_cost = min(cond_bases[powers[i]], min_cost)
   cond_bases[powers[i]] = min_cost

curr_powers_index, amount = 0, 0
for required_power in classes:
    while powers[curr_powers_index] < required_power:
       curr_powers_index += 1
    amount += cond_bases[powers[curr_powers_index]]

print(amount)