# import the necessary packages
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timezone
from datetime import timedelta

# construct an example date
date_example = date(year=2009, month=9, day=28)
print("date: {}".format(date_example))

# create an example time
time_example = time(hour=13, minute=59, second=24)
print("time: {}".format(time_example))

# access *both* the current date and time
now = datetime.now()
print("now: {}".format(now))

# create two datetime objects
earlier = datetime(2016, 11, 6, 8, 43, 2)
later = datetime(2017, 10, 31, 4, 14, 50)
print("earlier: {}".format(earlier))
print("later: {}".format(later))

# compute the difference (i.e., time delta) between the two datetime
# objects
delta = later - earlier

# display the elapsed days and seconds
print("elapsed days: {}".format(delta.days))
print("elapsed seconds: {}".format(delta.seconds))

# grab the current UTC time
utc_now = datetime.now(tz=timezone.utc)
print("utc now: {}".format(utc_now))

# create a time zone for UTC+11 (Sydney, Australia)
au_tz = timezone(timedelta(hours=11))
au_now = datetime.now(tz=au_tz)
print("sydney tz: {}".format(au_tz))
print("sydney now: {}".format(au_now))
