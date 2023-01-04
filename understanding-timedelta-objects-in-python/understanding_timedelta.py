# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timedelta

# when you create a timedelta object you can specify offsets in terms of
# days, seconds, microseconds, milliseconds, minutes, hours, and weeks,
# which will *automatically* be merged/consolidated into three attributes
# (days, seconds, and microseconds)
delta = timedelta(
    days=25,
    seconds=8,
    microseconds=10,
    milliseconds=7600,
    minutes=72,
    hours=16,
    weeks=4
)
print(delta)

# we can mix negative and positive values for attributes inside a timedelta
# object and the class will automatically handle merging and consolidation
# of the attributes
mixed_delta = timedelta(
    days=-5,
    seconds=300,
    minutes=-1,
    hours=72
)
print(mixed_delta)

# here is an example of how we can add 3 days to the current date and time
# utilizing a timedelta
now = datetime.now()
then = now + timedelta(days=3)
print("now: {}".format(now))
print("then: {}".format(then))

# we can also subtract a timedelta object from a datetime
now = datetime.now()
then = now - timedelta(days=3)
print("now: {}".format(now))
print("then: {}".format(then))

# ...which is the same as *adding* a timedelta with a *negative* attribute
now = datetime.now()
then = now + timedelta(days=-3)
print("now: {}".format(now))
print("then: {}".format(then))
