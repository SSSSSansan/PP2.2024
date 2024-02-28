import re
def cap(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(cap(input()))