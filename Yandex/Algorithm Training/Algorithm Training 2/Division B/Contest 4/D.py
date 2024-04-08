from collections import OrderedDict

fin = open('input.txt')

parties = OrderedDict()
all_votes = 0
for line in fin:
    *name, votes = line.split(); name = ' '.join(name); votes = int(votes)
    parties[name] = votes
    all_votes += votes
first_vote_num = all_votes / 450

places = dict()
all_places = 0
for party in parties:
    place = int(parties[party] // first_vote_num)
    places[party] = place
    all_places += place

if all_places < 450:
    remainder_votes = []

    for party in parties:
        remainder_votes.append((-(parties[party] % first_vote_num), parties[party], party))
    
    remainder_votes.sort()

    i = 0
    while all_places < 450:
        _, _, name = remainder_votes[i]
        places[name] += 1

        all_places += 1
        i = (i+1) % len(remainder_votes)

for party in parties:
    print(party, places[party])