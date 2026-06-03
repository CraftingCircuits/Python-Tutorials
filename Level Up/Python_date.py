# Python date time module and its functions
import datetime

# printing the current date
print("\n")
print("Current date:", datetime.date.today())

# understanding date output
# The date contains year, month, day, hour, minute, second, and microsecond.
current_datetime = datetime.datetime.now()
print("\n")
print("Current date and time:", current_datetime)
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)

# using strftime to format date output
print("\n")
x = datetime.datetime.now()
print(x.strftime("%B"))

# understanding the refrence of all the legal format code
print("\n")
# %a weekday, short version
print(x.strftime("%a"))
# %A weekday, full version
print("\n")
print(x.strftime("%A"))
# %b month, short version
print("\n")
print(x.strftime("%b"))
# %B month, full version
print("\n")
print(x.strftime("%B"))
# %w weekday as a number 0 - 6, 0 is sunday
print("\n")
print(x.strftime("%w"))
# %d day of month 01 - 31
print("\n")
print(x.strftime("%d"))
# %m month as a number 01-12
print("\n")
print(x.strftime("%m"))
# %y year, short version, without century
print("\n")
print(x.strftime("%y"))
# %Y year, full version
print("\n")
print(x.strftime("%Y"))
# %H hour 00-23
print("\n")
print(x.strftime("%H"))
# %I hour 00-12
print("\n")
print(x.strftime("%I"))
# %p AM or PM
print("\n")
print(x.strftime("%p"))
# %M minutes 00-59
print("\n")
print(x.strftime("%M"))
# %S seconds 00-59
print("\n")
print(x.strftime("%S"))
# %f microseconds 000000-999999
print("\n")
print(x.strftime("%f"))
# %z UTC offset
print("\n")
print(x.strftime("%z"))
# %Z timezone
print("\n")
print(x.strftime("%Z"))
# %j day number of year 001-366
print("\n")
print(x.strftime("%j"))
# %U week number of year, sunday as the first day of ween, 00-53
print("\n")
print(x.strftime("%U"))
# %W week number of year, monday as the first day of week, 00-53
print("\n")
print(x.strftime("%W"))
# %C local version of date and time
print("\n")
print(x.strftime("%C"))
# %x local version of date
print("\n")
print(x.strftime("%x"))
# %X local version of time
print("\n")
print(x.strftime("%X"))
# %% date and time in ISO 8601 format, A % cahracter is used to escape the % character
print("\n")
print(x.strftime("%%"))
# %G ISO 8601 week-based year
print("\n")
print(x.strftime("%G"))
# %u ISO 8601 weekday as a number 1-7
print("\n")
print(x.strftime("%u"))
# %V ISO 8601 week number of year, 01-53
print("\n")
print(x.strftime("%V"))
