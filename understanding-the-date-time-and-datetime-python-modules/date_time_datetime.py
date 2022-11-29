# DateTimeCoding.com

# import the necessary packages
import datetime
import time

# create an example date and display it
date_example = datetime.date(year=2019, month=3, day=3)
print("date: {}".format(date_example))

# demonstrate how to access the year, month, and day attributes of the
# date object
print("year: {}".format(date_example.year))
print("month: {}".format(date_example.month))
print("day: {}".format(date_example.day))

# grab the current date
today = datetime.date.today()
print("today: {}".format(today))

# an alternative method to obtain the current date is to grab the current
# unix timestamp and then construct a datetime object from it
today_alt = datetime.datetime.fromtimestamp(time.time())
print("today alternative: {}".format(today_alt))

# create an example time
time_example = datetime.time(hour=4, minute=32, second=9)
print("time: {}".format(time_example))

# demonstrate how to access the hour, minute, and second attributes of
# the time object
print("hour: {}".format(time_example.hour))
print("minute: {}".format(time_example.minute))
print("second: {}".format(time_example.second))

# construct a timezone for the east coast of the United States (UTC-5) and
# then use the timezone object to derive what time it currently is in New
# York
us_east_tz = datetime.timezone(datetime.timedelta(hours=-5))
us_east_now = datetime.datetime.now(tz=us_east_tz)
print("us east: {}".format(us_east_now))

# grab the current date and time for the time zone the machine is in
now = datetime.datetime.now()
print("now: {}".format(now))

# manually construct a datetime object
datetime_example = datetime.datetime(
    year=2018,
    month=6,
    day=2,
    hour=2,
    minute=47,
    second=34
)
print("datetime example: {}".format(datetime_example))

# access the year, month, and day of the datetime object
print("year: {}".format(datetime_example.year))
print("month: {}".format(datetime_example.month))
print("day: {}".format(datetime_example.day))

# access the hour, minute, second, microsecond, and any time zone info
print("hour: {}".format(datetime_example.hour))
print("minute: {}".format(datetime_example.minute))
print("second: {}".format(datetime_example.second))
print("microsecond: {}".format(datetime_example.microsecond))
print("tz info: {}".format(datetime_example.tzinfo))
