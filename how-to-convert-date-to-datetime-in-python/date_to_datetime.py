# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import date

# grab today's date
today = date.today()
print(type(today))
print("today: {}".format(today))

# construct the datetime object from the date object by manually
# supplying the year, month, and day attributes
dt = datetime(
    year=today.year,
    month=today.month,
    day=today.day
)
print(type(dt))
print("date to datetime: {}".format(dt))
