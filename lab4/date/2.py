from datetime import datetime, timedelta
curr = datetime.now()

yesterday = curr - timedelta(days=1)
tomorrow = curr + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", curr.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
