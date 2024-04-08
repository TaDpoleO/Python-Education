import math

GOLDEN_RATIO = (1+math.sqrt(5))/2

def eliminateY(x, y):
    turns = 0

    while y > 0:
        y = y-x
        x = x-y        
        turns += 1

        if x <= 0: return float('inf')

    return turns

def tactic(units_x, base_hp, units_y):
    turns = 1

    units_y -= (units_x-base_hp)
    units_x -= units_y

    turns += eliminateY(units_x, units_y)  

    return turns    

def last_turns(units_x, base_hp, units_y):
    if (2*units_x == units_y+base_hp) or ((units_y+base_hp-units_x)/(2*units_x-units_y-base_hp) >= GOLDEN_RATIO and units_x <= units_y): return float('inf')
    
    result = float('inf')

    turns0 = 0

    while (units_y+base_hp-units_x)/(2*units_x-units_y-base_hp) >= GOLDEN_RATIO:
        turns0 += 1
        base_hp -= (units_x-units_y)

    turns = tactic(units_x, base_hp, units_y)
    result = turns0+turns

    return min(result, turns0+1+tactic(units_x, base_hp-(units_x-units_y), units_y))

def answer(X, Y, P):
    turns = 1

    units_x = X
    base_hp = Y-X
    production = P

    if base_hp <= 0: return turns

    if units_x <= base_hp:
        if units_x <= production: return -1
        
        K = (base_hp-units_x) // (units_x-production)
        turns += K
        base_hp -= (units_x-production)*K

    turns += last_turns(units_x, base_hp, production)

    if turns == float('inf'):
        return -1
    else:
        return turns

def main():
    fin = open('input.txt')
    X = int(fin.readline())
    Y = int(fin.readline())
    P = int(fin.readline())

    print(answer(X, Y, P))

if __name__ == '__main__':
    main()