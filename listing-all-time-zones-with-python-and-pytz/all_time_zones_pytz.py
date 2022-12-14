# DateTimeCoding.com

# import the necessary packages
import pytz

# grab the *common* set of time zones built into pytz
print("COMMON TIME ZONES")
print("=" * 17)
common_tz = pytz.common_timezones

# loop over the common time zones and display them
for tz in common_tz:
    print(tz)

# grab the big set of *ALL* time zones in pytz
print("ALL TIME ZONES")
print("=" * 14)
all_tz = pytz.all_timezones

# loop over all the time zones and display them
for tz in all_tz:
    print(tz)
