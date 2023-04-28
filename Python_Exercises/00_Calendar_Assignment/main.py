from input import Input
from process import Process
from output import Output

year_object = Input()
year = year_object.year
process_object = Process()
print_output = Output(year)
print_output.print_header()
print_output.print_body()




