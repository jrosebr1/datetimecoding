# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timezone
import time

# we can use the 'time' module to grab the current unix timestamp
time_unix_ts = time.time()
print("time unix timestamp: {}".format(time_unix_ts))

# similarly, we can use 'datetime' to grab the unix timestamp
now = datetime.now()
datetime_unix_ts = now.timestamp()
print("now: {}".format(now))
print("datetime unix timestamp: {}".format(datetime_unix_ts))

# another option is to use 'timetuple'
now = datetime.now()
timetuple_unix_ts = now.timetuple()
print("now: {}".format(now))
print("timetuple unix timestamp: {}".format(datetime_unix_ts))

# if we use the 'datetime' module then we can construct unix timestamps
# for arbitrary dates; let's see the unix timestamp for 1:05:00PM UTC
# for thanksgiving 2022
thanksgiving = datetime(2022, 11, 24, 13, 5, 0, tzinfo=timezone.utc)
thanksgiving_unix_ts = thanksgiving.timestamp()
print("utc thanksgiving: {}".format(thanksgiving))
print("utc thanksgiving unix timestamp: {}".format(thanksgiving_unix_ts))

# if we leave off the 'tzinfo' attribute we can get the thanksgiving unix
# timestamp for our local timezone (I'm in America/New_York which is UTC-5
# so your output will be different than mine depending on your timezone)
thanksgiving = datetime(2022, 11, 24, 13, 5, 0)
thanksgiving_unix_ts = thanksgiving.timestamp()
print("local thanksgiving: {}".format(thanksgiving))
print("local thanksgiving unix timestamp: {}".format(thanksgiving_unix_ts))
