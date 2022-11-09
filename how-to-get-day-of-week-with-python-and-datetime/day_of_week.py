# DateTimeCoding.com

# import the necessary packages
from datetime import datetime

# define a list of human-readable day names
day_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# grab the current date and time, and display the day of the week
now = datetime.now()
print("now: {}".format(now))

# we can use the 'weekday' method to grab the integer index of the weekday,
# where 0 is monday and 6 is sunday
i = now.weekday()
print("weekday integer: {}".format(i))
print("weekday name: {}".format(day_names[i]))

# let's see what day of the week christmas falls
christmas = datetime(2022, 12, 25)
i = christmas.weekday()
print("christmas integer: {}".format(i))
print("christmas name: {}".format(day_names[i]))
