import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_anniversary(year, month, day):
    return datetime.date(year + 1, month, day)

def previous_anniversary(year, month, day):
    return datetime.date(year - 1, month, day)

def check_anniversary(year, month, day):
    anniversary = datetime.date(year, month, day)
    if is_leap_year(year):
        print("Leap year! Next anniversary:", next_anniversary(year, month, day))
    else:
        print("Not a leap year. Previous anniversary:", previous_anniversary(year, month, day))

# Test the function
year = int(input("Enter the year of the anniversary: "))
month = int(input("Enter the month of the anniversary: "))
day = int(input("Enter the day of the anniversary: "))

check_anniversary(year, month, day)
