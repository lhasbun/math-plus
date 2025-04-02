import math

class Square:
    """A class to represent a square.\nAttributes:\n
    side_length (float): The length of the side of the square.\n
    Attributes (auto-calculated by constructor):\n
    area (float): The area of the square.\n
    perimeter (float): The perimeter of the square.\n
    diagonal (float): The length of the diagonal of the square."""

    def __init__(self, side_length):
        self.side_length = side_length
        self.area = self.area()
        self.perimeter = self.perimeter()
        self.diagonal = self.diagonal()

    def area(self) -> float:
        """Calculate the area of the square.\n
        Formula: Area = side * side or Area = side^2"""
        return self.side_length ** 2

    def perimeter(self) -> float:
        """Calculate the perimeter of the square.\n
        Formula: Perimeter = 4 * side"""
        return 4 * self.side_length
    
    def diagonal(self) -> float:
        """Calculate the length of the diagonal of the square.\n
        Formula: Diagonal = side * √2"""
        return self.side_length * math.sqrt(2)
    
class Rectangle:
    """"A class to represent a rectangle.\nAttributes:\n length (float): The length of the rectangle.\n"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the area of the rectangle.\n
        Formula: Area = length * width"""
        return self.length * self.width
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.\n
        Formula: Perimeter = 2 * (length + width)"""
        return 2 * (self.length + self.width)
    
    def diagonal(self) -> float:
        """Calculate the length of the diagonal of the rectangle.\n
        Formula: Diagonal = √(length^2 + width^2)"""
        return math.sqrt(self.length ** 2 + self.width ** 2)