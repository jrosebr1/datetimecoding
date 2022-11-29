# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import pendulum
import arrow


def is_tz_aware(d):
    # if there is no time zone info then the datetime object is *not*
    # time zone aware
    if d.tzinfo is None:
        return False

    # otherwise, there is time zone information...but we also need to
    # ensure there is a UTC offset
    elif d.tzinfo.utcoffset(d) is None:
        return False

    # all checks have passed so the datetime object is time zone aware
    return True


# grab the current datetime for the machine's local time (i.e., *not*
# time zone aware)
tz_unaware = datetime.now()
print("datetime: {}".format(tz_unaware))
print("is_tz_aware: {}".format(is_tz_aware(tz_unaware)))

# grab the current datetime, this time indicating that we want UTC
# (implying that the datetime object *is* time zone aware)
tz_aware = datetime.now(tz=timezone.utc)
print("datetime: {}".format(tz_aware))
print("is_tz_aware: {}".format(is_tz_aware(tz_aware)))

# grab the current date and time for the local time zone
now = datetime.now()
print("local: {}".format(now))

# construct a timezone for Tokyo (UTC+9) and then use the timezone object
# to derive what time it currently is in Tokyo
tokyo_tz = timezone(timedelta(hours=9))
tokyo_now = datetime.now(tz=tokyo_tz)
print("toyko: {}".format(tokyo_now))

# use pendulum to grab the current date and time in Tokyo
tokyo_now_pendulum = pendulum.now(tz="Asia/Tokyo")
print("tokyo pendulum: {}".format(tokyo_now_pendulum))

# use arrow to obtain the current date and time in Tokyo
tokyo_now_arrow = now_arrow = arrow.now(tz="Asia/Tokyo")
print("arrow pendulum: {}".format(tokyo_now_arrow))
