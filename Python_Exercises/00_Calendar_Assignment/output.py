class Output:
    def __init__(self, year) -> None:
        self.year = str(year)
        
    def print_header(self):
        width = 35
        title_year = self.year
        # make title_year appear in the middle
        print("{:^{width}}".format(title_year, width=width))
        print("_" * width)
        