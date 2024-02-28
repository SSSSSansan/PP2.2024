#ex1
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
#ex2
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#ex3
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
#ex4
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#ex5
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

