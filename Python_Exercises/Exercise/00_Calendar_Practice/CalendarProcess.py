months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
END_MONTH = 12
START_DAY_OF_1800 = 3

def get_valid_month(month_str: str):
    for idx in range(len(months)):
        if month_str.capitalize() == months[idx].capitalize() or month_str.capitalize() == months[idx][:3].capitalize():
            return idx + 1
    try:
        month = int(month_str)
        if 1 <= month <= END_MONTH:
            return month
    except ValueError:
        return None
    return None

def is_leap_year(year: int):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
    
def get_total_days_of_month(year: int, month: int):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31
    
def get_month_name(month: int):
    return months[month - 1]

def get_start_day(year: int, month: int):
    start_day = START_DAY_OF_1800
    for year_idx in range(1800, year):
        start_day += 366 if is_leap_year(year_idx) else 365

    for month_idx in range(1, month):
        d = get_total_days_of_month(year, month_idx)
        start_day += d
    return start_day % 7