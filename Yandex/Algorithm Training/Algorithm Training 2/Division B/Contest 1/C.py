fin = open('input.txt')
x, y, year = [int(x) for x in fin.readline().split()]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def isCorrectDate(day, month, year):
    day_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if isLeapYear(year): day_in_month[2] = 29

    if month > 12: return False
    if day > day_in_month[month]: return False

    return True

def answer(x, y, year):
    var1 = isCorrectDate(x, y, year)
    var2 = isCorrectDate(y, x, year)

    if var1 and var2:
        if x == y:
            return 1
        else:
            return 0
    else:
        return 1

print(answer(x, y, year))