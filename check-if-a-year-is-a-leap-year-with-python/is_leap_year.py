# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
import calendar

# we can check if an arbitrary year is a leap year or not by using
# python's built-in 'calendar' module and the 'isleap()' method
year = 2019
leap = calendar.isleap(year)
print("Q. Is {} a leap year? A. {}".format(year, leap))

# loop over all years between 1990 and now
for year in range(1990, datetime.now().year):
    # check to see if the current year is a leap year or not
    leap = calendar.isleap(year)
    print("Q. Is {} a leap year? A. {}".format(year, leap))
