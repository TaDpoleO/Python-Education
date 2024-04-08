MONTH_MAP = {
    'January':      1,
    'February':     2,
    'March':        3,

    'April':        4,
    'May':          5,
    'June':         6,

    'July':         7,
    'August':       8,
    'September':    9,

    'October':      10,
    'November':     11,
    'December':     12,
}

DAY_OF_WEEK_MAP = {
    'Monday':       0,
    'Tuesday':      1,
    'Wednesday':    2,
    'Thursday':     3,
    'Friday':       4,
    'Saturday':     5,
    'Sunday':       6,

    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

def is_leap_year(year):
    if year % 400 == 0: return True

    if year % 4 == 0 and (year % 100) != 0:
        return True
    else:
        return False

def get_days_in_month(year, month):
    DAYS_IN_MONTH_MAP = {
        1: 31, 
        2: 28,
        3: 31,

        4: 30,
        5: 31,
        6: 30,

        7: 31,
        8: 31,
        9: 30,

        10: 31,
        11: 30,
        12: 31,   
    }

    if is_leap_year(year): DAYS_IN_MONTH_MAP[2] += 1

    return DAYS_IN_MONTH_MAP[month]

def main():
    fin = open('input.txt')
    N = int(fin.readline())    
    year = int(fin.readline())

    holidays = set()
    for _ in range(N):
        day, month = fin.readline().split()
        day = int(day)
        month = MONTH_MAP[month]

        holidays.add((month, day))

    week_day = [0]*7
    holidays_day = [0]*7

    first_day = DAY_OF_WEEK_MAP[fin.readline().rstrip()]

    days_in_year = 365
    if is_leap_year(year): days_in_year += 1  

    cur_day, cur_month = 1, 1
    cur_day_of_week = first_day

    for _ in range(1, days_in_year+1):
        if (cur_month, cur_day) in holidays:
            holidays_day[cur_day_of_week] += 1
        week_day[cur_day_of_week] += 1

        cur_day_of_week = (cur_day_of_week+1) % 7

        cur_day += 1
        if cur_day > get_days_in_month(year, cur_month):
            cur_day = 1
            cur_month += 1

    total_holidays = sum(holidays_day)
    for i in range(7):
        week_day[i] += total_holidays-holidays_day[i]
    
    best_and_worst = [(total, i) for i, total in enumerate(week_day)]
    best_and_worst.sort()

    print(DAY_OF_WEEK_MAP[best_and_worst[6][1]], DAY_OF_WEEK_MAP[best_and_worst[0][1]])


if __name__ == '__main__':
    main()