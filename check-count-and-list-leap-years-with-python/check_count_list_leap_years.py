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
for year in range(1990, datetime.now().year + 1):
    # check to see if the current year is a leap year or not
    leap = calendar.isleap(year)
    print("Q. Is {} a leap year? A. {}".format(year, leap))


# set the start and end year range we are interested in
start_year = 1995
end_year = 2022

# count the number of leap years there are between two input years
num_leap_years = calendar.leapdays(start_year, end_year)
print("there are {} leap years between '{}' and '{}'".format(
    num_leap_years, start_year, end_year
))

# determine which *specific* years are leap years between two input
# year ranges
leap_years = [y for y in range(start_year, end_year + 1)
              if calendar.isleap(y)]
print("the leap years are: {}".format(leap_years))
