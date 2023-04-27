def print_header(month_name: str, year: int):
    width = 35
    string = month_name + " " + str(year)
    print("{:^{width}}".format(string, width=width))
    print("-" * width)

def print_body(start_day: int, total_days: int):
    day_width = 5
    print(" Sun  Mon  Tue  Wed  Thu  Fri  Sat")
    print(" ", end="")
    print(" " * day_width * start_day, end="")
    next_day = start_day
    for day in range(1, total_days + 1):
        print(format(day, "3d") + "  ", end="")
        next_day += 1
        if next_day % 7 == 0:
            print()
            print(" ", end="")

    