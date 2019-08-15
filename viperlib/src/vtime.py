import datetime
import time
from viperlib.src.misc import strdigit_normalize

def current_time_24h():
    """Returns current time in format hh:mm:ss"""
    return time.strftime("%H:%M:%S")

def secs2time(secs):
    """Converts integer number of seconds to a time string of format hh:mm:ss."""
    h = secs//(60*60)
    m = (secs-h*60*60)//60
    s = secs-(h*60*60)-(m*60)
    x = [ h, m, s ]
    for i in range(len(x)):
        if x[i] < 10:
            x[i] = '0' + str(x[i])
        x[i] = str(x[i])
    return ':'.join(x)

def time2secs(timestr):
    """Converts time in format hh:mm:ss to number of seconds."""
    h, m, s = timestr.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def tsleep(timestr):
    """Custom sleep: pauses execution for time period in format hh:mm:ss. """
    time.sleep(time2secs(timestr))

def timefromnow(plustime):
    """Returns time in format hh:mm:ss which is in hh:mm:ss from now as specified by the argument."""
    res = secs2time(time2secs(current_time_24h()) + time2secs(plustime))
    res = res.split(':')
    if int(res[0]) >= 24 : res[0] = strdigit_normalize(str(int(res[0])%24))
    return ':'.join(res)

def timestamp():
    """Returns timestamp in format dd-MMM hh:mm PM/AM."""
    return datetime.datetime.now().strftime("%d-%b %I:%M %p")
