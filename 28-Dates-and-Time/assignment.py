from datetime import date, time

# Declare a titanic variable pointing to a date object representing April 14th, 1912
titanic = date(1912, 4, 14)
# Declare an independence_day variable pointing to a date object representing July 4th, 1776
independence_day = date(1776, 7, 4)
# Declare an alarm_clock variable set to a time object representing 05:45:00AM
alarm_clock = time(5, 45)
# Declare a one_second_away variable set to a time object representing 11:59:59PM
one_second_away = time(23, 59, 59)

from datetime import datetime

# Define a one_from_two function that accepts a date object and a time object
def one_from_two(date, time):
    return datetime(
        date.year, date.month, date.day, time.hour, time.minute, time.second
    )


# It should return a datetime object consisting of
#     - the year, month and day from the date object
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime
# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)
# one_from_two(some_date, some_time) => datetime object representing 2002-02-22 09:45:23
