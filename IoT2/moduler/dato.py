from datetime import datetime
import pytz  # module for working with time zones

def dato1():
    tz = pytz.timezone('Europe/Oslo')  # specify the time zone
    now = datetime.now(tz)  # get the current datetime object in the specified time zone
    timer_minutter = now.strftime("%H:%M")  # format the datetime object as hours and minutes only

    return timer_minutter

def dato2():
    tz = pytz.timezone('Europe/Oslo')  # specify the time zone
    now = datetime.now(tz)  # get the current datetime object in the specified time zone
    år_måned_dag = now.strftime("%Y/%m/%d")  # format the datetime object as year, month and day only

    return år_måned_dag