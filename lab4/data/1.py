from datetime import datetime, timedelta


date = datetime.now()


new_date = date - timedelta(days=5)


print(date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))
