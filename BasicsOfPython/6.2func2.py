import datetime as dt

def record_time(msg, time=dt.datetime.now().date()):

    print('{:}, time: {:}'.format(msg,time))

record_time("Hello")
record_time("Hello","Jan, 1, 2020")