from datetime import datetime, timedelta
curr = datetime.now()
result = curr - timedelta(days=5)

print("Current date:", curr.strftime("%Y-%m-%d"))
print("Five days ago:", result.strftime("%Y-%m-%d"))
