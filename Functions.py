def is_year_leap(year): # True or false is returned if the year is a leap year or not
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True


def days_in_month(year, month): # None is returned for invalid year or month, True is returned otherwise
    if year < 1582 or month < 1 or month > 12:
        return None
    
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    res = days[month -1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res


def day_of_year(year, month, day): #iterate through every month via invoking days_in_month() to tally all days in the year
 
    total = 0
    for months in range(1,month):
        md = days_in_month(year,months)
        if md == None: 
            return None
        total += md
    md = days_in_month(year,month)
    if md != None and day <= md and day > 0:
        total += day
    else:
        return None
    return "Corresponding day is " + str(total) + " in the year " + str(year)
    
print(day_of_year(2000, 11, 31))
print(day_of_year(1999, 2, 29))
print(day_of_year(2000, 12, 33))
print(day_of_year(1999, -1, 29))
print(day_of_year(1999, 2, 29))
print(day_of_year(2000, 1, -1))
print(day_of_year(2000, 1, 0))
print(day_of_year(2000, 12, 31))
