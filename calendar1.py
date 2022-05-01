import calendar

# dec = calendar.TextCalendar(calendar.SUNDAY)
# result = dec.prmonth(2022, 5)
# print(result)
# print(type(result))

# print(calendar.prcal(2022))


year = int(input('Enter the year to display as a webpage: '))

with open("C:/my_develop2/python_basic/files/yearly_calendar.html", "w") as cal:
    cal.write(calendar.HTMLCalendar(calendar.SUNDAY).formatyear(year))