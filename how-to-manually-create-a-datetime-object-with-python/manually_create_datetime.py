# DateTimeCoding.com

# import the necessary packages
from datetime import datetime

# manually create a datetime object
dt = datetime(2013, 3, 25, 10, 44, 47)
print("datetime: {}".format(dt))

# re-create the same datetime object, but this time use the keyword
# arguments to made the code less ambiguous/easier to read
dt = datetime(
    year=2013,
    month=3,
    day=25,
    hour=10,
    minute=44,
    second=47
)
print("datetime w/ keyword args: {}".format(dt))

# create a datetime for a specific date at midnight
dt = datetime(2018, 6, 1, 0, 0, 0)
print("datetime at midnight: {}".format(dt))

# create a datetime object for hours that are PM (note the use of a
# 24-hour clock when constructing datetime objects with python)
dt = datetime(
    year=2015,
    month=10,
    day=29,
    hour=20,
    minute=20,
    second=29
)
print("datetime w/ 24-hour clock: {}".format(dt))

# create a datetime object with a microsecond component
dt = datetime(
    year=2022,
    month=10,
    day=24,
    hour=17,
    minute=49,
    second=16,
    microsecond=459061
)
print("datetime w/ microsecond: {}".format(dt))
