# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
import pendulum
import arrow

# use the datetime library to grab current date and time
now_dt = datetime.now()
print("datetime now: {}".format(now_dt))

# grab the current date and time separately, then combine it into a
# datetime object
now_date = datetime.now().date()
now_time = datetime.now().time()
now_combined = datetime(
    year=now_date.year,
    month=now_date.month,
    day=now_date.day,
    hour=now_time.hour,
    minute=now_time.minute,
    second=now_time.second,
    microsecond=now_time.microsecond
)
print("date and time combined now: {}".format(now_dt))

# use the pendulum library to get the current date and time
now_pendulum = pendulum.now()
print("pendulum now: {}".format(now_dt))

# use the arrow library to get the current date and time
now_arrow = arrow.now()
print("arrow now: {}".format(now_dt))
