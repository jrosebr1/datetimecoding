# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
import pytz

# create two time zone *naive* datetime objects that we'll be taking the
# difference between
naive_dt_a = datetime(2022, 11, 1, 7, 0, 5)
naive_dt_b = datetime(2020, 1, 1, 0, 0, 0)
print("first time zone naive date: {}".format(naive_dt_a))
print("second time zone naive date: {}".format(naive_dt_b))

# compute the difference between the naive datetime objects
naive_diff = naive_dt_a - naive_dt_b
print("naive diff: {}".format(naive_diff))
print("naive days: {}".format(naive_diff.days))
print("naive total seconds: {}".format(naive_diff.total_seconds()))

# create two time zone *aware* datetime objects that we'll also take the
# difference between
aware_dt_a = datetime(2022, 11, 10, 13, 13, 13,
                      tzinfo=pytz.timezone("America/New_York"))
aware_dt_b = datetime(2020, 3, 11, 10, 0, 0,
                      tzinfo=pytz.timezone("UTC"))
print("first time zone aware date: {}".format(aware_dt_a))
print("second time zone aware date: {}".format(aware_dt_b))

# compute the difference between the aware datetime objects
aware_diff = aware_dt_a - aware_dt_b
print("aware diff: {}".format(aware_diff))
print("aware days: {}".format(aware_diff.days))
print("aware total seconds: {}".format(aware_diff.total_seconds()))

# if we try to take the difference between an aware and a naive object,
# we'll get an error
diff = aware_dt_a - naive_dt_b
