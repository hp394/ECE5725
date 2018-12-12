import time
def getHour():
    t = time.localtime(time.time())
    timestring = time.asctime(t)
    timestamp = timestring.split()
    return timestamp[3].split(':')[0]
def getMin():
    t = time.localtime(time.time())
    timestring = time.asctime(t)
    timestamp = timestring.split()
    return timestamp[3].split(':')[1]
'''
t = time.localtime(time.time())
timestring = time.asctime(t)
timestamp = timestring.split()
weekday = timestamp[0]
month = timestamp[1]
day = timestamp[2]
hour = timestamp[3].split(':')[0]
minute = timestamp[3].split(':')[1]
sec = timestamp[3].split(':')[2]
year = timestamp[4]
print(weekday)
print(month)
print(day)
print(hour)
print(minute)
print(sec)
print(hour)
print(year)
'''
