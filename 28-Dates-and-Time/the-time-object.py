from datetime import time

start = time()  # 1. using the time class constructor
print(start)  # by default, the time is set to 00:00:00
print(type(start))
# print(start.hour)
# print(start.minute)
# print(start.second)
# print(start.microsecond)

print(time(6))
print(time(6, 30))
print(time(6, 30, 45))

print(time(12, 25))

evening = time(hour=18, minute=30, second=45)
print(evening)
# there are some restrictions on the values of the arguments
# print(time(25, 30, 45))  # ValueError: hour must be in 0..23
# print(time(12, 60, 45))  # ValueError: minute must be in 0..59
# print(time(12, 30, 60))  # ValueError: second must be in 0..59
