# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timezone

# set the unix timestamp to be December 7th, 1988 UTC
unix_ts = 597456000

# convert the unix timestamp to a datetime object (the *problem* with
# this approach is that a timezone wasn't supplied so your system will
# convert the datetime to your local time, which may or may not be what
# you intend)
dt = datetime.fromtimestamp(unix_ts)
print(dt)

# the best way to avoid the ambiguity is to work in UTC time, which
# produces the intended result
dt = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
print(dt)

# now that the unix timestamp has been converted to a datetime object
# we can access the year, month, day, etc. attributes as we normally
# would
print("year: {}".format(dt.year))
print("month: {}".format(dt.month))
print("day: {}".format(dt.day))
print("hour: {}".format(dt.hour))
print("minute: {}".format(dt.minute))
print("second: {}".format(dt.second))
print("timezone: {}".format(dt.tzname()))

# from there we can format the date in a variety of human-readable formats
print(dt.strftime("%D"))
print(dt.strftime("%b %d %Y"))
print(dt.strftime("%Y-%m-%d %H:%M"))
print(dt.strftime("%A, %B %-d %Y at %-H:%M:%S%p %Z"))
