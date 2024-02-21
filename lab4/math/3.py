import math

def pol():
    s = int(input("Input number of sides:"  ))
    l = int(input("Input the length of a side:" ))
    area = (s*l**2)/(4 * math.tan(math.pi / s))
    return area
print("The area of the polygon is:", pol())

