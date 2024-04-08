MAX_SECS_IN_DAY = 86400 # 24*60*60

def timeToTimeInSec(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

def timeInSecToTime(time_in_secs):
    hours = time_in_secs//3600
    minutes = (time_in_secs-hours*3600)//60
    seconds = time_in_secs-hours*3600-minutes*60
    
    return f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}'

def normalizeTimeInSecsToDay(time_in_secs):    
    if time_in_secs >= 0:
        return time_in_secs % MAX_SECS_IN_DAY
    else:
        while time_in_secs < 0:
            time_in_secs += MAX_SECS_IN_DAY
        return time_in_secs

fin = open('input.txt')

h1, m1, s1 = [int(x) for x in fin.readline().split(':')]
h2, m2, s2 = [int(x) for x in fin.readline().split(':')]
h3, m3, s3 = [int(x) for x in fin.readline().split(':')]

time_s1 = timeToTimeInSec(h1, m1, s1)
time_s2 = timeToTimeInSec(h2, m2, s2)
time_s3 = timeToTimeInSec(h3, m3, s3)

send_time = ((time_s3-time_s1))/2
gap = (time_s2-time_s1-send_time)
exact_time = int(normalizeTimeInSecsToDay(time_s3+gap)+0.5)

print(timeInSecToTime(exact_time))