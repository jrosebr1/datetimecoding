# DateTimeCoding.com

# import the necessary packages
from datetime import datetime


def compare_datetime(date_a, date_b):
    # check to see if the first date is *earlier* than the second one
    if date_a < date_b:
        return -1

    # check to see if the first date is *later* than the second one
    elif date_a > date_b:
        return 1

    # otherwise, the two dates are *equal*
    return 0


# create two datetime objects where the first date is *before* the second
# date
first_date = datetime(2022, 12, 5, 12, 30, 0)
second_date = datetime(2022, 12, 6, 1, 0, 0)
print("first: {}".format(first_date))
print("second: {}".format(second_date))

# check to see if the first date is *later* than the second one
if compare_datetime(first_date, second_date) == 1:
    print("'{}' is *later* than '{}'".format(first_date, second_date))

# check to see if the first date is *earlier* than the second one
elif compare_datetime(first_date, second_date) == -1:
    print("'{}' is *earlier* than '{}'".format(first_date, second_date))

# otherwise, the two dates are *equal*
else:
    print("'{}' is *equal to* '{}'".format(first_date, second_date))

# reset the two datetime objects, this time making the first date *after*
# the second date
first_date = datetime(2022, 12, 25, 0, 0, 0)
second_date = datetime(2022, 1, 1, 5, 22, 1)
print("first: {}".format(first_date))
print("second: {}".format(second_date))

# check to see if the first date is *later* than the second one
if compare_datetime(first_date, second_date) == 1:
    print("'{}' is *later* than '{}'".format(first_date, second_date))

# check to see if the first date is *earlier* than the second one
elif compare_datetime(first_date, second_date) == -1:
    print("'{}' is *earlier* than '{}'".format(first_date, second_date))

# otherwise, the two dates are *equal*
else:
    print("'{}' is *equal to* '{}'".format(first_date, second_date))

# reset the datetime objects again, this time making them equal
first_date = datetime(2022, 12, 25)
second_date = datetime(2022, 12, 25)
print("first: {}".format(first_date))
print("second: {}".format(second_date))

# check to see if the first date is *later* than the second one
if compare_datetime(first_date, second_date) == 1:
    print("'{}' is *later* than '{}'".format(first_date, second_date))

# check to see if the first date is *earlier* than the second one
elif compare_datetime(first_date, second_date) == -1:
    print("'{}' is *earlier* than '{}'".format(first_date, second_date))

# otherwise, the two dates are *equal*
else:
    print("'{}' is *equal to* '{}'".format(first_date, second_date))
