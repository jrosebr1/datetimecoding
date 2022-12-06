# DateTimeCoding.com

# import the necessary packages
from threading import Thread
from datetime import datetime
from datetime import timedelta
import time


def reminder_task(reminder, sleep_count=1):
    # keep looping until our reminder date/time is reached
    while True:
        # grab the current date and time
        now = datetime.now()

        # check to see if the current datetime is past our reminder
        # datetime, indicating that the user should be alerted
        if now >= reminder:
            print("REMINDER!!! ({})".format(now))
            return

        # sleep for a small amount of time until we check the current
        # date and time again
        time.sleep(sleep_count)


# grab the current date and time
now = datetime.now()
print("now: {}".format(now))

# set our reminder date (i.e., when the "reminder alarm" should go off
# to be 10 seconds in the future)
reminder_dt = now + timedelta(seconds=10)
print("reminder date: {}".format(reminder_dt))

# spawn a thread that will run in the background, checking to see if
# the reminder should go off
print("waiting for reminder to go off...")
t = Thread(target=reminder_task, args=(reminder_dt,), daemon=True)
t.start()
t.join()

# if you don't want to use a timedelta you can construct an arbitrary
# datetime object in the future (depending on when you run the code to
# this post it's *highly likely* that the hardcoded date and time here
# has already past, which is why I recommend using 'timedelta' objects)
reminder_dt = datetime(2022, 12, 6, 11, 14, 0)
print("new reminder date: {}".format(reminder_dt))

# spawn a thread that will run in the background, checking to see if
# the reminder should go off
print("waiting for reminder to go off...")
t = Thread(target=reminder_task, args=(reminder_dt,), daemon=True)
t.start()
t.join()
