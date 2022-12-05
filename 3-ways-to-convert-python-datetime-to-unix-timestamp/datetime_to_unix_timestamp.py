# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from time import mktime
import pendulum
import arrow

# use the default datetime library to grab the current time and convert
# it to a unix timestamp
dt_now = datetime.now()
dt_ts = dt_now.timestamp()
print("datetime timestamp: {}".format(dt_ts))

# if you're using a python version *older* than v3.3, then you need to
# use the 'timetuple' and 'mktime' methods as the 'timestamp' method is
# not available
mktime_now = datetime.now()
mktime_ts = mktime(mktime_now.timetuple())
print("mktime timestamp: {}".format(mktime_ts))

# use pendulum to grab the current date and time, convert it to a unix
# timestamp, and then display the integer portion of the timestamp only,
# leaving off any fractional information
pendulum_now = pendulum.now()
pendulum_ts = pendulum_now.timestamp()
print("pendulum timestamp: {}".format(pendulum_ts))
print("pendulum int timestamp: {}".format(pendulum_now.int_timestamp))

# utilize arrow to grab the current date and time, derive the unix timestamp,
# and then display the normal unix timestamp and the integer portion
arrow_now = arrow.now()
arrow_ts = arrow_now.timestamp()
print("arrow timestamp: {}".format(arrow_ts))
print("arrow int timestamp: {}".format(arrow_now.int_timestamp))
