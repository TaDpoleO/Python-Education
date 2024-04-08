def getAdStarts(events):
    if not events: return 0, 10, 20

    best_start1 = best_start2 = 0
    best_customers_count = 0

    curr_customers = set()
    for i in range(len(events)):
        start1, event_type1, id_customer1 = events[i]
        if event_type1 == TYPE_IN: curr_customers.add(id_customer1)

        if len(curr_customers) > best_customers_count:
            best_start1 = start1
            best_start2 = start1+10  
            best_customers_count = len(curr_customers)
        
        best_customer_count2 = 0
        for j in range(i+1, len(events)):
            start2, event_type2, id_customer2 = events[j]
            if (event_type2 == TYPE_IN) and (id_customer2 not in curr_customers): best_customer_count2 += 1

            if (start2 <= start1-5 or start2 >= start1+5) and (len(curr_customers)+best_customer_count2 > best_customers_count):
                best_start1 = start1
                best_start2 = start2
                best_customers_count = len(curr_customers)+best_customer_count2

            if (event_type2 == TYPE_OUT) and (id_customer2 not in curr_customers): best_customer_count2 -= 1

        if event_type1 == TYPE_OUT: curr_customers.remove(id_customer1)  

    return best_customers_count, *sorted([best_start1, best_start2])

fin = open('input.txt')
N = int(fin.readline())

TYPE_IN = 0
TYPE_OUT = 10

events = []
for i in range(N):
    t1, t2 = [int(x) for x in fin.readline().split()]
    if t2-t1 >= 5:
        events.append((t1, TYPE_IN, i))
        events.append((t2-5, TYPE_OUT, i))
events.sort()

print(*getAdStarts(events))