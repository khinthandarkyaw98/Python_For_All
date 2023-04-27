import datetime

YEAR = "year"
MONTH = "month"
START_YEAR = 1800
END_YEAR = datetime.datetime.now().year + 100


def get_year() -> int:
    continued = True
    while continued:
        try:
            year = int(input("Enter full year: "))
            if START_YEAR <= year <= END_YEAR:
                continued = False
            else:
                print("Enter a year between", START_YEAR, "and", END_YEAR)
        except ValueError:
            print("Please enter a valid")
    return year



def get_month() -> int:
    return input("Enter month: ")