class Process():
    def __init__(self, year:int) -> None:
        self.year = year
        
    def is_leap_year(self) -> bool:
        year = self.year
        return ((year % 100 != 100 and year % 4 == 0) or year % 400 == 0)
    