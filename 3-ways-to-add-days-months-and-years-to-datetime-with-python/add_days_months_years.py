# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timedelta
import pendulum
import arrow

# grab the current date and time
now = datetime.now()
print("now: {}".format(now))

# add 10 days to the current date
then = now + timedelta(days=10)
print("+10 days: {}".format(then))

# add three years to the current date
then = now + timedelta(days=365 * 3)
print("+3 years: {}".format(then))

# grab the current date and time with pendulum
now = pendulum.now()
print("pendulum now: {}".format(now))

# add 4 days to the current date with pendulum
then = now.add(days=4)
print("+4 days: {}".format(then))

# add 8 months to the current date with pendulum
then = now.add(months=8)
print("+8 months: {}".format(then))

# add 2 years from the current date with pendulum
then = now.add(years=2)
print("+2 years: {}".format(then))

# combine adding 4 days 8 months, and 2 years into a single function
# call with pendulum
then = now.add(days=4, months=8, years=2)
print("+4 days, +8 months, +2 years: {}".format(then))

# for what it's worth we can also subtract time deltas with pendulum...
then = now.subtract(weeks=3)
print("-3 weeks: {}".format(then))

# ...which is the equivalent of adding -3 weeks
then = now.add(weeks=-3)
print("-3 weeks w/ add: {}".format(then))

# grab the current date and time with arrow
now = arrow.now()
print("arrow now: {}".format(now))

# subtract 2 months from the current date and time with arrow
then = now.shift(months=-2)
print("-2 months: {}".format(then))

# add 10 days and 5 years to the current date with arrow
then = now.shift(days=10, years=5)
print("+5 days, +10 years: {}".format(then))