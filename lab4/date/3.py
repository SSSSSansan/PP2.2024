from datetime import datetime
curr= datetime.now()

result = curr.replace(microsecond=0)

print("Original datetime:", curr)
print("Datetime without microseconds:", result)
