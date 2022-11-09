# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timezone

# grab the datetime object associated with the start of the unix epoch
# which is January 1st, 1970 (UTC)
unix_epoch = datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)
print("unix epoch: {}".format(unix_epoch))

# grab the current datetime (in UTC) and then derive the total number of
# seconds and milliseconds between the current datetime and the unix epoch
now = datetime.now(tz=timezone.utc)
seconds = (now - unix_epoch).total_seconds()
print("now: {}".format(now))
print("seconds: {}".format(seconds))
print("milliseconds: {}".format(seconds * 1000))

# we can also do the same thing for arbitrary datetime objects; here are
# the total number of seconds and milliseconds between my birthday,
# December 7th, 1988 at 12:07:43PM UTC
birthday = datetime(
    year=1988,
    month=12,
    day=7,
    hour=12,
    minute=7,
    second=43,
    tzinfo=timezone.utc
)
seconds = (birthday - unix_epoch).total_seconds()
print("birthday: {}".format(birthday))
print("seconds: {}".format(seconds))
print("milliseconds: {}".format(seconds * 1000))
