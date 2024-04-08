from collections import defaultdict
inp_file = open('input.txt')

TYPE_DEPOSIT = 'DEPOSIT' # 3
TYPE_WITHDRAW = 'WITHDRAW' # 3
TYPE_BALANCE = 'BALANCE' # 2
TYPE_TRANSFER = 'TRANSFER' # 4
TYPE_INCOME = 'INCOME' # 2

records = defaultdict(int)
for line in inp_file:
    transaction = line.split()
    if transaction[0] == TYPE_DEPOSIT:
        client, money = transaction[1], int(transaction[2])
        records[client] += money
    elif transaction[0] == TYPE_WITHDRAW:
        client, money = transaction[1], int(transaction[2])
        records[client] -= money
    elif transaction[0] == TYPE_BALANCE:
        client = transaction[1]
        if client in records:
            print(records[client])
        else:
            print('ERROR')
    elif transaction[0] == TYPE_TRANSFER:
        client1, client2, money = transaction[1], transaction[2], int(transaction[3])
        records[client1] -= money
        records[client2] += money
    elif transaction[0] == TYPE_INCOME:
        procent = int(transaction[1])
        for client, money in records.items():
            if money > 0:
                records[client] = records[client]+int(records[client]*procent/100)