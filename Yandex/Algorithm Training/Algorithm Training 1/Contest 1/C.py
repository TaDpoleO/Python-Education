inp_file = open('input.txt')

def getPhoneNumber(s):
    s = s.replace('-', '')
    lengthS = len(s)
    
    if s[0] == '+':
        if lengthS == 14:
            return '8'+s[3:6]+s[7:]
        elif lengthS == 12:
            return '8'+s[2:5]+s[5:]
        else:
            return '8495'+s[2:]
    else:
        if lengthS == 13:
            return '8'+s[2:5]+s[6:]
        elif lengthS == 11:
            return s
        elif lengthS == 8:
            return '8'+s[1:4]+s[4:]            
        else: # lengthS == 7
            return '8495'+s


new_phone = getPhoneNumber(inp_file.readline().rstrip())
for curr_phone in inp_file:
    if new_phone == getPhoneNumber(curr_phone.rstrip()):
        print('YES')
    else:
        print('NO')