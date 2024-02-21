from datetime import datetime

date1 = datetime(input())  
date2 = datetime(input()) 

difference = abs((date2 - date1).total_seconds())
print("The difference between the two dates is:", difference, "seconds")
