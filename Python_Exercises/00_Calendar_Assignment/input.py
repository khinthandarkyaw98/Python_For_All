import datetime

class Input:
    start_year = 1800
    end_year = datetime.datetime.now().year + 100
    def __init__(self) -> None:
        continued = True
        while continued:
            try: 
                self.year = int(input("Enter the full year : "))
                year = self.year
                if self.start_year <= year <= self.end_year:
                    continued = False
            except ValueError:
                print("Please enter a valid year in NUMBER ")
                
        

    
    