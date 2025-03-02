class Shape:
    def __init__(self, width):
        self.width = width

class Square(Shape):
    name = "Square"
    def get_area(self):
        return self.width**2
    
class Triangle(Shape):
    name = "Triangle"
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return 0.5*self.width*self.height

SquareX = Square(5)
print("Bentuk:", SquareX.name, "& Luas:", SquareX.get_area(), "cm^2")
TriangleY = Triangle(5, 3)
print("Bentuk:", TriangleY.name, "& Luas:", TriangleY.get_area(), "cm^2")