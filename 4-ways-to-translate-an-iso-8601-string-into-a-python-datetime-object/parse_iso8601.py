# DateTimeCoding.com

# import the necessary packages
from datetime import datetime
from dateutil import parser
import pendulum
import arrow


def display_parsed_iso8601(name, dt):
    # display the name of the datetime parser
    print(name)
    print("=" * len(name))

    # write the year, month day, hour, minute, second, and timezone to
    # the terminal
    print("year: {}".format(dt.year))
    print("month: {}".format(dt.month))
    print("day: {}".format(dt.day))
    print("hour: {}".format(dt.hour))
    print("minute: {}".format(dt.minute))
    print("second: {}".format(dt.second))
    print("time zone: {}\n".format(dt.tzname()))


# create an example ISO 8601 string
iso8601_example = "2014-01-07T15:50-04:00"

# use the datetime library to parse the ISO 8601 string
dt = datetime.fromisoformat(iso8601_example)
display_parsed_iso8601("standard datetime", dt)

# use the dateutil library to parse the ISO 8601 string
dateutil_dt = parser.parse(iso8601_example)
display_parsed_iso8601("dateutil", dateutil_dt)

# use the pendulum library to parse the ISO 8601 string
pendulum_dt = pendulum.parse(iso8601_example)
display_parsed_iso8601("pendulum", pendulum_dt)

# use the arrow library to parse the ISO 8601 string
arrow_dt = arrow.get(iso8601_example).datetime
display_parsed_iso8601("arrow", arrow_dt)
