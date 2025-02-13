from datetime import datetime, timedelta

data = datetime.now()
data_before = data - timedelta(days=1)
data_after = data + timedelta(days=1)

print(data_before.strftime("%Y-%m-%d"))
print(data.strftime("%Y-%m-%d"))
print(data_after.strftime("%Y-%m-%d"))