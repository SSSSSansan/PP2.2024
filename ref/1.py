class Circle:
    def __init__(self, rad ):
        self.rad  = rad
    def area (self):
        print(self.rad * self.rad == 0)  

class Shape(Circle):
    def __init__(self, rad = 0 ):
        self.rad  = rad
    def area (self) :
        print((self.rad **2)*3.14) 

p = Shape()
p.area()