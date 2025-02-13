from datetime import datetime

now = datetime.now()
print(now)

now_without = now.replace(microsecond=0)

print(now_without)