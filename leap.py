def is_leap_year(year):
    if year_divisible_by_four(year):
    # if year % 100 == 0 and year % 400 == 0:
    #     return True
    # if year % 4 == 0 and year % 400 == 0:
    #     return True
    # elif year % 100 == 0 and year % 4 == 0:
    #     return False
    # else:
    #     return False

def year_divisible_by_four(year):
    if year % 4 == 0:
        return True

def year_divisible_by_100(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    if year % 100 == 0 and year % 400 != 0:
        return False 


# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400
