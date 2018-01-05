import time
import datetime


def creatTimeStamp(datestr, format='%Y-%m-%d'):
    return time.mktime(time.strptime(datestr, format))


def creatTimeStr(timestamp, format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.fromtimestamp(timestamp).strftime(format)
