from collections import OrderedDict

fin = open('input.txt', encoding='utf8')
N = int(fin.readline())

max_references = 1
topics, messages = OrderedDict(), dict()
for i in range(1,N+1):
    code = int(fin.readline())
    if code == 0:
        subject = fin.readline().rstrip()
        message = fin.readline().rstrip()
        topics[i] = [subject, 1]
        messages[i] = 0
    else:
        message = fin.readline().rstrip()
        messages[i] = code

        curr_code = i
        while messages[curr_code] != 0:
            curr_code = messages[curr_code]

        topics[curr_code][1] += 1
        if topics[curr_code][1] > max_references: max_references =  topics[curr_code][1]

for key in topics:
    if topics[key][1] == max_references:
        print(topics[key][0])
        break