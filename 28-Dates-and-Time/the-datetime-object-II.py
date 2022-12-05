from datetime import datetime

today = datetime.today()

print("month", today.strftime("%m"))
print("day", today.strftime("%d"))
print("year", today.strftime("%Y"))  # %Y is the year in 4 digits
print("year", today.strftime("%y"))  # 2-digit year
print("hour", today.strftime("%H"))
print("minute", today.strftime("%M"))
print("second", today.strftime("%S"))
print("year/month/day", today.strftime("%Y/%m/%d"))
print("day of the week", today.strftime("%A"))
print("month name", today.strftime("%B"))
