def trap():
    h = int(input("Height:" ))
    f = int(input("Base, first value:" ))
    s = int(input("Base, second value: "))
    area = ((f+s)*h)/2
    return area
print("Expected Output:", trap())