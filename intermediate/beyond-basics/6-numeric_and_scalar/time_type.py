import datetime

datetime.time(3)            # 3h
datetime.time(3, 1)         # 3h 1m
datetime.time(3, 1, 2)      # 3h 1m 2s
datetime.time(3, 1, 2, 262) # 3h 1m 2s 262us

datetime.time(hour=23, minute=59, second=59, microsecond=999999)

t = datetime.time(10, 59, 15, 8923)
t.hour              # 10
t.minute            # 59
t.second            # 15
t.microsecond       # 8923

t.isoformat()               # '10:59:15.8923'
t.strftime('%Hh%Mm%Ss')     # '10h59m15s'
