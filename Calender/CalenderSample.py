import calendar

# Create an Plain text Calender

# Selection of starting day, Here we have selected an SUNDAY
c = calendar.TextCalendar(calendar.SUNDAY)
# Selection of Year and month , Here we have selected 2019 and Feb
str = c.formatmonth(2019,2)
# Printing an String / Calendar
print(str)
