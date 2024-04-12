from collections import defaultdict

def getDividers(number):    
    dividers = defaultdict(int)
    if number == 1: return {1: 1}

    start = 2
    while start <= (number // 2):
        if number % start == 0:
            dividers[start] += 1
            number = number // start
        else:
            start += 1

    if not dividers:
        return {number: 1}
    else:
        dividers[number] += 1
        return dividers
    
def reduceDividers(numerator, denominator):
    for key in denominator:
        if key in numerator:
            min_count = min(numerator[key], denominator[key])
            numerator[key] -= min_count
            denominator[key] -= min_count
    
    return numerator, denominator

def getNumberFromDividers(dividers):
    res = 1

    for key, val in dividers.items():
        res *= key**val

    return res

def answer(a, b, c, d):
    numerator = getDividers(a*d+c*b)
    denominator = getDividers(b*d)

    numerator, denominator = [getNumberFromDividers(x) for x in reduceDividers(numerator, denominator)]
    if numerator == 0:
        return 1, 1
    else:
        return numerator, denominator

fin = open('input.txt')
a, b, c, d = [int(x) for x in fin.readline().split()]

print(*answer(a, b, c, d))