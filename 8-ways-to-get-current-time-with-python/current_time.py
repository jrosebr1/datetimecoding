# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
import pendulum
import arrow
import pytz
import time

# grab the current time using datetime and display the result
# to our screen
now_dt = datetime.now()
print("using datetime: {}".format(now_dt))

# another way to grab the current time is to grab the 'time' object
# associated with the datetime
now_dt_time = datetime.now().time()
now_time_formatted = now_dt_time.strftime("%H:%M:%S")
print("using datetime and time: {}".format(now_time_formatted))

# we can use the 'time' module to grab the current time and then
# format it
now_time = time.localtime()
time_formatted = time.strftime("%H:%M:%S", now_time)
print("time formatted: {}".format(time_formatted))

# using pytz we can grab the time in a specific time zone with
# datetime
tokyo_tz = pytz.timezone("Asia/Tokyo")
now_dt_tz = datetime.now(tz=tokyo_tz)
print("using datetime and pytz: {}".format(now_dt_tz))

# pendulum can also be easily used to grab the current time
now_pendulum = pendulum.now().time()
print("using pendulum: {}".format(now_pendulum))

# and we can also use pendulum to set the time zone for the
# current time
now_pendulum_tz = pendulum.now(tz="Asia/Kolkata").time()
print("using pendulum w/ time zone: {}".format(now_pendulum_tz))

# the arrow library can be used to grab the current time
now_arrow = arrow.now().time()
print("using arrow: {}".format(now_arrow))

# arrow can also be used to grab the current time in time zones *other*
# than your system time
now_arrow_tz = now_arrow = arrow.now(tz="US/Pacific").time()
print("using arrow w/ time zone: {}".format(now_arrow_tz))
