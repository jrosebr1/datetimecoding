# DateTimeCoding.com

# import the necessary packages
from datetime import datetime

# grab the current datetime
now = datetime.now()
print("now: {}".format(now))

# extract only the time portion of the datetime
time_only = now.time()
print(type(time_only))
print("time only: {}".format(time_only))

# grab the hour, minute, second, microsecond, and timezone (if any) from
# the time object
print("hour: {}".format(time_only.hour))
print("minute: {}".format(time_only.minute))
print("second: {}".format(time_only.second))
print("microsecond: {}".format(time_only.microsecond))
print("time zone: {}".format(time_only.tzname()))
