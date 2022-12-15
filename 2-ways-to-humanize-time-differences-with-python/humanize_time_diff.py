# DateTimeCoding.com

# import the necessary packages
import pendulum
import arrow

# grab the current date and time using pendulum
now = pendulum.now()

# subtract a day from the current date and get the human-readable
# difference
delta = now.subtract(days=1)
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(delta.diff_for_humans()))

# if we combine multiple resolutions into a single operation then
# pendulum will default to the *lowest* granularity (in this case,
# days)
delta = now.subtract(days=5, hours=17)
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(delta.diff_for_humans()))

# here is another example of how the lowest granularity will be
# used when computing the humanized difference
delta = now.add(hours=3, minutes=16, seconds=1)
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(delta.diff_for_humans()))

# grab the current date and time using arrow
now = arrow.now()

# use arrow to shift the current date two weeks into the future
# and then make the difference human-readable
delta = now.shift(weeks=2)
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(delta.humanize()))

# shift the current date 10 hours into the past and then humanize it
delta = now.shift(hours=-10)
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(delta.humanize()))

# shift the current date and time 6 days, 22 minutes and 55 seconds
# into the future, but show the human-readable date difference in
# total minutes (i.e., convert days and seconds to minutes)
delta = now.shift(days=6, minutes=22, seconds=55)
humanized = delta.humanize(granularity="minute")
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(humanized))

# shift the current date 6 days, 22 minutes, and 55 seconds into
# the past, then show the humanized difference in days and minutes
# (leaving off any second information)
delta = now.shift(days=-6, minutes=-22, seconds=-55)
humanized = delta.humanize(granularity=["day", "minute"])
print("now: {}".format(now))
print("delta: {}".format(delta))
print("humanized: {}".format(humanized))
