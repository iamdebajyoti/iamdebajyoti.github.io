import datetime
import dateutil
from dateutil.relativedelta import relativedelta

old = datetime.date(2002,6,1)
today1 = datetime.datetime.today()
cur = datetime.date(today1.year, today1.month, today1.day)
datediff = relativedelta(cur, old)
print(f"{datediff.years} years, {datediff.months} months and {datediff.days} days")

if datediff.month