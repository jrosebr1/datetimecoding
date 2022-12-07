# DateTimeCoding.com

# import the necessary packages
from datetime import datetime


def calculate_age(born):
    # grab the current date and
    today = datetime.now()

    # determine if today's month and day precede the birth month and
    # day (1 if true, 0 otherwise)
    precede = int((today.month, today.day) < (born.month, born.day))

    # calculate the year difference between the current year and birth
    # year, taking into account whether today's month and day precede
    # the birth month and day
    age = (today.year - born.year) - precede

    # return the computed age
    return age


# compute my age
birthday = datetime(1988, 12, 7).date()
age = calculate_age(birthday)
print("born: {}, age: {}".format(birthday, age))
