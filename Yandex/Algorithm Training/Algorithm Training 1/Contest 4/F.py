from collections import defaultdict
inp_file = open('input.txt')

customers = defaultdict(lambda: defaultdict(int))
for line in inp_file:
    customer, product, amount = line.split()
    customers[customer][product] += int(amount)
    
for customer in sorted(customers.keys()):
   print(f'{customer}:')
   for product in sorted(customers[customer].keys()):
       print(f'{product} {customers[customer][product]}')