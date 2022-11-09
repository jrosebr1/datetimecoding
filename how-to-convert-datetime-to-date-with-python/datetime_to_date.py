# DateTimeCoding.com

# import the necessary packages
from datetime import datetime

# grab the current datetime
now = datetime.now()
print("now: {}".format(now))

# extract only the date portion of the datetime
date_only = now.date()
print(type(date_only))
print("date only: {}".format(date_only))

# grab the year, month, and day from the date object
print("year: {}".format(date_only.year))
print("month: {}".format(date_only.month))
print("day: {}".format(date_only.day))
