import calendar

# Create an Plain text Calender
# Selection of starting day, Here we have selected an SUNDAY
c = calendar.TextCalendar(calendar.MONDAY)


# Selection of Year and month , Here we have selected 2019 and Feb
str = c.formatmonth(2019,2)
# Printing an String / Calendar
print("Calendar of Feb 2019:" ,str)


# Printing the calendar dates also using For loop
for i in c.itermonthdates(2019,2) :
 print("Dates of the months are:" ,i)


# Printing calendar days also using for Loop
for m in c.itermonthdays(2019,2):
    print("Days of the Months are :" ,m)

for months in calendar.month_name:
 print("Month Names are :",months)

 for days in calendar.day_name:
     print("Month Names are :", days)