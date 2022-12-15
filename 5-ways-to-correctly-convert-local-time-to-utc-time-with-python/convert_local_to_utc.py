# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pendulum
import arrow
import pytz
import time

# grab the current local time (which is by default a *naive* datetime
# object with no time zone information associated with it)
local_time = datetime.now()
print("{} (local time)".format(local_time))

# a verbose (and potentially buggy) way of converting a datetime object
# to UTC time is to first determine the UTC offset (converting seconds
# to hours), and then use a timedelta object to correct for the UTC\
# offset
utc_offset = time.timezone if time.localtime().tm_isdst == 0 \
    else time.altzone
utc_offset /= (60 * 60) * -1
utc_time = local_time - timedelta(hours=utc_offset)
print("{} (utc offset)".format(utc_offset))
print("{} (naive utc conversion)".format(utc_time))

# a nicer way to convert local time zone to UTC is to use the 'astimezone'
# method built into the datetime library
utc_tz = local_time.astimezone(timezone.utc)
print("{} (datetime utc conversion)".format(utc_tz))

# if you use the 'pytz' library you can also directly specify the timezone
# (this is often the preferred method since it gives you more control, just
# in case you want to specify a time zone *other than* UTC)
utc_tz = pytz.timezone("UTC")
utc_time = local_time.astimezone(utc_tz)
print("{} (pytz utc conversion)".format(utc_time))

# the pendulum library makes it trivially easy to convert a local datetime
# to UTC time
local_time = pendulum.now()
utc_time = local_time.in_tz("UTC")
print("{} (pendulum local time)".format(local_time))
print("{} (pendulum utc conversion)".format(utc_time))

# similarly, arrow makes it easy to convert a local date and time to UTC time
local_time = arrow.now()
utc_time = local_time.to("utc")
print("{} (arrow local time)".format(local_time))
print("{} (arrow utc conversion)".format(utc_time))
