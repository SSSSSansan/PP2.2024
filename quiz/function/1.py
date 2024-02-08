def calculate():
    x = int(input())
    i = 1
    sum = 1
    while i<=x:
        sum=i*sum
        i+=1
    return sum 

print(calculate())