import datetime 

datetime.datetime(2020, 1, 22, 10, 59, 15, 8923)
datetime.datetime(year=2020, month=1, day=22, hour=10, minute=59, second=15, microsecond=8923)

datetime.datetime.today()
datetime.datetime.now()         # similar to today() but can manage timezones
datetime.datetime.utcnow()

datetime.datetime.fromtimestamp(1000000000)     # 2001-09-08 20:46:40
datetime.datetime.fromordinal(713239)           # 1953-10-13 00:00:00

''' combine date and time types '''
d = datetime.date.today()
t = datetime.time(8, 15)
datetime.datetime.combine(d, t)         # 2020-01-22 08:15:00

dt = datetime.datetime.strptime('Monday 6 January 2014, 12:13:31',
                                '%A %d %B %Y, %H:%M:%S')
dt.date()       # datetime.date(2014, 1, 6)
dt.time()       # datetime.time(12, 13, 31)


''' Arithmetic with datetime '''

a = datetime.datetime(year=2014, month=5, day=8, hour=14, minute=22)
b = datetime.datetime(year=2014, month=3, day=14, hour=12, minute=9)
d = a - b           # datetime.timedelta(55, 7980)

datetime.date.today() + datetime.timedelta(weeks=1) * 3     # 2020-02-12


''' Timezones '''
cot = datetime.timezone(datetime.timedelta(hours=1), "COT")
# datetime.timezone(datetime.timedelta(seconds=3600), 'COT')
departure = datetime.datetime(year=2014, month=1, day=7,
                                hour=11, minute=30, tzinfo=cot)
arrival = datetime.datetime(year=2014, month=1, day=7,
                            hour=13, minute=5, tzinfo=datetime.timezone.utc)
duration = arrival - departure
repr(duration)      # datetime.timedelta(seconds=9300)
str(duration)       # 2:35:00

