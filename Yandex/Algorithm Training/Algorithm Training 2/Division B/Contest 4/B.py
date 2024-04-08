from collections import defaultdict

fin = open('input.txt')
votes = defaultdict(int)

for line in fin:
    candidate, vote = line.split(); vote = int(vote)
    votes[candidate] += vote
    
for key in sorted(votes):
    print(key, votes[key])