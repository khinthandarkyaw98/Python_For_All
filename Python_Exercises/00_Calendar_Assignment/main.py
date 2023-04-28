from input import Input
from process import Process
from output import Output

Year = Input()
year = Year.year
isLeap = Process(year)
check = isLeap.is_leap_year()
print_ = Output(year)
print_.print_header()


