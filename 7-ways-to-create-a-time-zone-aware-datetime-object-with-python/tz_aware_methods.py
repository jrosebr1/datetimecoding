# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timezone
import pytz
import pendulum
import arrow

# grab the current date and time that is *naive* and has *no* time
# zone information associated with it
naive_now = datetime.now()
print("{} (naive)".format(naive_now))

# grab the current date and time again, but make this one *aware* by
# associating the UTC time zone with it
aware_now = datetime.now(tz=timezone.utc)
print("{} (aware in UTC time zone)".format(aware_now))

# the default 'timezone' package built into python isn't very helpful
# outside of UTC aware datetime objects, so if we want to create a time
# zone aware object in time zones *other than* UTC we should use 'pytz'
est_tz = pytz.timezone("US/Pacific")
est_now = datetime.now(tz=est_tz)
print("{} (PST time zone)".format(est_now))

# here's another example using 'pytz', but let's create an aware datetime
# object for Qatar
qatar_tz = pytz.timezone("Asia/Qatar")
qatar_now = datetime.now(tz=qatar_tz)
print("{} (Qatar time zone)".format(qatar_now))

# by default, pendulum will create a time zone aware datetime object
pendulum_now = pendulum.now()
print("{} (pendulum w/ aware datetime)".format(pendulum_now))

# the arrow package gives us time zone aware datetime objects by default
# as well
arrow_now = arrow.now()
print("{} (arrow w/ aware datetime)".format(arrow_now))

# if you instead want to *manually* construct a datetime object that is
# time zone aware, just combine 'datetime' and 'pytz'
aware = datetime(2010, 6, 25, 2, 33, 3,
                 tzinfo=pytz.timezone("Africa/Cairo"))
print("{} (pytz aware in Cairo time zone)".format(aware))

# another way to create a time zone aware object is to instantiate it with
# pendulum
pendulum_dt = pendulum.datetime(1997, 8, 2, 6, 33, 20, tz="Europe/Madrid")
print("{} (pendulum aware in Madrid time zone)".format(pendulum_dt))

# manually creating a time zone aware object with datetime and arrow
arrow_dt = arrow.get(
    datetime(2015, 1, 9, 12, 42, 47),
    "Indian/Maldives"
)
print("{} (arrow aware in Maldives time zone)".format(arrow_dt))
