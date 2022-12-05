# import datetime
from datetime import date

# there are 3 ways to create a date object

# 1. using the date class constructor
# date(year, month, day)
d1 = date(2000, 8, 29)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)


# 2. using the today() method
d2 = date.today()
print(d2)

# 3. using the fromtimestamp() method
# fromtimestamp(timestamp)
d3 = date.fromtimestamp(0)
print(d3)
