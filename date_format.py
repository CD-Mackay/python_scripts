from datetime import date

date_today = date.today()

print("The date today is :%d-%d-%d" % (date_today.day, date_today.month, date_today.year))

custom_date = date(2021, 4, 5)

print("The custom date is: ", custom_date)