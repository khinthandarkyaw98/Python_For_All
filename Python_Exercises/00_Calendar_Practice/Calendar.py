import CalendarInput, CalendarOutput, CalendarProcess

year = CalendarInput.get_year()
valid = False
while not valid:
    month = CalendarInput.get_month()
    month = CalendarProcess.get_valid_month(month)
    valid = month
    if not valid:
        print("Enter a valid month.")
total_days = CalendarProcess.get_total_days_of_month(year, month)
CalendarOutput.print_header(CalendarProcess.get_month_name(month), year)
CalendarOutput.print_body(CalendarProcess.get_start_day(year, month), total_days)