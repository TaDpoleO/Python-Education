inp_file = open('input.txt')

troom, tcond = [int(x) for x in inp_file.readline().split()]
mode = inp_file.readline().rstrip()

def answer(troom, tcond, mode):
    if mode == 'freeze':
        return min(troom, tcond)
    elif mode == 'heat':
        return max(troom, tcond)
    elif mode == 'auto':
        return tcond
    else:
        return troom
    
    
print(answer(troom, tcond, mode))