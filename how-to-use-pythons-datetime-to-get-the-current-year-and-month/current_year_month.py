# DateTimeCoding.com

# import the necessary packages
from datetime import datetime

# grab the current date and time
today = datetime.now()
print("today: {}".format(today))

# we can access the year and month attributes like so
print("year: {}".format(today.year))
print("month: {}".format(today.month))
