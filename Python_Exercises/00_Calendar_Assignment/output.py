"""_summary_
    print Header in the center
    print months of the year(user_input)
"""
from process import Process

class Output():
    width = 35
    def __init__(self, year:int) -> None:
        self.year = year
        
    def print_header(self):
        title_year = str(self.year)
        # make title_year appear in the middle
        print("{:^{width}}".format(title_year, width=self.width))
        print("-" * self.width)
        
    def print_body(self):
        day_width = 5 # bc "Sun  "
        process = Process()
        for month_idx, month in enumerate(process.months):
            print("{:^{width}}".format(month, width=self.width))
            print(" Sun  Mon  Tue  Wed  Thu  Fri  Sat")
            print(" ", end="")
            start_day_of_the_month = process.get_start_day(self.year, month_idx)
            print(" " * day_width * start_day_of_the_month, end="") 
            total_days_of_month = process.get_total_days_of_month(self.year, month_idx) 
            next_day = start_day_of_the_month
            for day in range(1, total_days_of_month + 1):
                print(format(day, "3d") + "  ", end="")
                next_day += 1
                if next_day % 7 == 0:
                    print()
                    print(" ", end="") 
            print("\n\n")
            
            