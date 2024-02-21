class MyShape:
    def __init__(self, color="black", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0


class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=False, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return (f"Rectangle - {super().__str__()}, "
                f"Top Left: ({self.x_top_left}, {self.y_top_left}), "
                f"Length: {self.length}, Width: {self.width}")


class Circle(MyShape):
    def __init__(self, color="black", is_filled=False, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return (f"Circle - {super().__str__()}, "
                f"Center: ({self.x_center}, {self.y_center}), "
                f"Radius: {self.radius}")


def create_rectangle_from_input():
    color = input("Enter color of rectangle: ")
    is_filled = input("Is rectangle filled? (True/False): ").lower() == "true"
    x_top_left = int(input("Enter x coordinate of top left corner: "))
    y_top_left = int(input("Enter y coordinate of top left corner: "))
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))
    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)


if __name__ == "__main__":
    rectangle = create_rectangle_from_input()
    print(rectangle)
    print("Area:", rectangle.getArea())
