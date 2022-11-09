# DateTimeCoding.com

# import the necessary packages
from datetime import datetime

# grab the current date and time
now = datetime.now()
print("now: {}".format(now))

# the datetime object consists of *both* a 'date' and 'time' component
# (hence the name 'datetime')
print("date: {}".format(now.date()))
print("time: {}".format(now.time()))

# let's access the year, month, and day components of the date
print("year: {}".format(now.year))
print("month: {}".format(now.month))
print("day: {}".format(now.day))

# similarly, we can access the hour, minute, second, and microsecond of
# the time
print("hour: {}".format(now.hour))
print("minute: {}".format(now.minute))
print("second: {}".format(now.second))
print("microsecond: {}".format(now.microsecond))
