"""_summary_
    1 Jan 1800 : Wednesday 
    Sunday = 0
    Saturday = 0
    Wednesday = 0
"""
class Process():
    start_day_of_1800 = 3
    months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
        
    def is_leap_year(self, year:int) -> bool:
        return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
    
    def get_total_days_of_month(self, year:int, month:int) -> int:
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        if month == 2:
            return 29 if self.is_leap_year(year) else 28
        else:
            return 31
    
    def get_start_day(self, year:int) -> int:
        start_day = self.start_day_of_1800
        for year_idx in range(1800, year):
            # count all the days of years before this year
            start_day += 366 if self.is_leap_year(year_idx) else 365 
        return start_day % 7
    
    
            
        
            
            
    
        
    