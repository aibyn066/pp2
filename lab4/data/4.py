from datetime import datetime

d1 = input("input YYYY-MM-DD: ")
d2 = input('input YYYY-MM-DD: ')

date1 = datetime.strptime(d1,'%Y-%m-%d')
date2 = datetime.strptime(d2,'%Y-%m-%d')

date3 = (date2-date1).total_seconds()
print(date3)