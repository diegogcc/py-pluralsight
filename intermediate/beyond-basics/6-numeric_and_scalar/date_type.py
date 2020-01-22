import datetime

datetime.date(2014, 1, 6)       # YMD
# datetime.date(2014, 1, 6)
datetime.date(year=2014, month=1, day=6)
# datetime.date(2014, 1, 6)

datetime.date.today()       # today's date
datetime.date.fromtimestamp(1000000000)     # datetime.date(2001, 9, 9)
datetime.date.fromordinal(713239)           # 1953-10-13     <-    days from year 1

# Today is wednesday
d = datetime.date.today()
d.year          # 2020
d.month         # 1
d.day           # 22
d.weekday       # 2
d.isoweekday    # 3    <--   index starts at 1
d.isoformat     # '2020-01-22'
d.strftime('%A %d %B %Y')               # Wednesday 22 January 2020
'The date is {:%A %d %B %Y}'.format(d)  # 'The date is Wednesday 22 January 2020'
# Best use:
e= datetime.date(2020, 1, 22)
'{date:%A} {date.day} {date:%B} {date.year}'.format(date=e) # Wednesday 22 January 2020

