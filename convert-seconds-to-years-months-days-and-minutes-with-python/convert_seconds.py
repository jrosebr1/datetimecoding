# DateTimeCoding.com

# import the necessary packages
from collections import OrderedDict
from datetime import datetime


def convert_seconds(seconds):
    # take the input number of seconds, divide it by 60 to derive the
    # total number of whole minutes (quotient), leaving the remainder
    # as seconds
    (minutes, seconds) = divmod(seconds, 60)

    # do the same thing again, but this time divide the number of
    # minutes by 60, yielding the number of hours
    (hours, minutes) = divmod(minutes, 60)

    # now that we have the number of hours, we can determine the
    # whole number of days
    (days, hours) = divmod(hours, 24)

    # finally, given the number of days, we can derive the whole
    # number of years
    (years, days) = divmod(days, 365)

    # construct a dictionary representing the timeframe
    timeframe = OrderedDict([
        ("years", years),
        ("days", days),
        ("hours", hours),
        ("minutes", minutes),
        ("seconds", seconds),
    ])

    # return the timeframe dictionary
    return timeframe


# grab the current date and time
now = datetime.now()

# construct an arbitrary datetime in the past, compute the delta
# between the two dates (deriving the total number of elapsed
# seconds), and then convert the seconds into years, months,
# days, minutes, and seconds
then = datetime(2022, 12, 1, 0, 0, 0)
delta = (now - then).total_seconds()
converted = convert_seconds(delta)
print("now: {}".format(now))
print("then: {}".format(then))
print("converted: {}".format(converted))

# construct another example of an arbitrary datetime in the past,
# then determine the number of years, months, days, and minutes
# that have passed
then = datetime(1995, 4, 24, 7, 38, 38)
delta = (now - then).total_seconds()
converted = convert_seconds(delta)
print("now: {}".format(now))
print("then: {}".format(then))
print("converted: {}".format(converted))

# create a datetime object for a point in the *future*, compute
# the number of seconds difference between now and then (notice
# how the order of the date subtraction is now *SWAPPED*), and
# finally derive the number of years, months, days, and minutes
# that will have to pass until we arrive at the future date
then = datetime(2025, 3, 18, 17, 45, 1)
delta = (then - now).total_seconds()
converted = convert_seconds(delta)
print("now: {}".format(now))
print("then: {}".format(then))
print("converted: {}".format(converted))
