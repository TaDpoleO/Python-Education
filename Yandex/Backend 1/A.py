fin = open('input.txt')

N = int(fin.readline())

candidates = [('', '', '', 0, 0, 0)]*N
for i in range(N):
    lastname, firstname, fathername, day, month, year = fin.readline().split(',')
    day, month, year = [int(x) for x in (day, month, year)]

    candidates[i] = (lastname, firstname, fathername, day, month, year)

def cipher(candidate):
    lastname, firstname, fathername, day, month, year = candidate

    letters_count = len(set(lastname) | set(firstname) | set(fathername))

    digits_sum = 0
    while day != 0:
        digits_sum += day % 10
        day = day // 10

    while month != 0:
        digits_sum += month % 10
        month = month // 10

    first_letter_of_lastname_index = ord(lastname[0].lower())-96

    res_sum = letters_count + digits_sum*64 + first_letter_of_lastname_index*256
    hex_sum = hex(res_sum)[2:]
    
    if len(hex_sum) < 3: hex_sum = '0'*(3-len(hex_sum))+hex_sum
    
    return hex_sum[-3:].upper()

for candidate in candidates:
    print(cipher(candidate), end=' ')