# it's not a date but represents a duration of time
# it's a difference between two dates or times
from datetime import timedelta, datetime

birthday = datetime(2000, 8, 29)
today = datetime.now()
days_alive = today - birthday
print(days_alive)
print(type(days_alive))

print(days_alive.total_seconds())

five_hundred_days = timedelta(days=500)
