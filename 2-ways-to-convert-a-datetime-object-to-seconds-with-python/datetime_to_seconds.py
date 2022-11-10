# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timezone

# grab the datetime object associated with the start of the unix epoch
# which is January 1st, 1970 (UTC)
unix_epoch = datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)
print("unix epoch: {}".format(unix_epoch))

# set the input datetime object
input_dt = datetime(2005, 7, 4, 14, 33, 21, tzinfo=timezone.utc)
print("input datetime: {}".format(input_dt))

# compute the total number of seconds between the unix epoch and the
# input datetime object
total_seconds = (input_dt - unix_epoch).total_seconds()
print("total seconds: {}".format(total_seconds))

# construct another datetime time
another_dt = datetime(2003, 12, 24, 23, 59, 59, tzinfo=timezone.utc)
print("another datetime: {}".format(another_dt))

# compute the total number of seconds between the two dates
total_seconds = (input_dt - another_dt).total_seconds()
print("total seconds: {}".format(total_seconds))
