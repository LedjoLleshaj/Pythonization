from datetime import datetime  # module datetime != class datetime

print(datetime(2000, 8, 29))
print(datetime(2000, 8, 29, 12, 30, 45))

print("Now =>", datetime.now())
print("Today =>", datetime.today())
print(
    datetime.today() == datetime.now()
)  # false because they will never run at the same time so they will never be equal

today = datetime.today()
today.replace(
    year=2020
)  # the only way to make changes to a datetime object is to create a new one
