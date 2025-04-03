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
    """"A class to represent a rectangle.\nAttributes:\n 
    length (float): The length of the rectangle.\n 
    width (float): The width of the rectangle.\n"""

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
    
class Triangle:
    """A class to represent a triangle.\nAttributes:\n 
    side_a (float): The length of side a of the triangle.\n 
    side_b (float): The length of side b of the triangle.\n 
    side_c (float): The length of side c of the triangle.\n"""

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """Calculate the area of the triangle.\n
        Formula: Using Heron's formula: Area = √[s(s - a)(s - b)(s - c)] where ( s = (a + b + c)/2 )"""
        s = ((self.side_a + self.side_b + self.side_c) / 2 )
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle.\n
        Formula: Perimeter = a + b + c"""
        return self.side_a + self.side_b + self.side_c
    
    def pythagorean_theorem(self) -> bool:
        """Check if the triangle satisfies the Pythagorean theorem.\n
        Formula: a^2 + b^2 = c^2"""
        # Sort the sides to identify the longest side
        sides = sorted([self.side_a, self.side_b, self.side_c])
        self.side_a, self.side_b, self.side_c = sides
        return (self.side_a ** 2 + self.side_b ** 2 == self.side_c ** 2)
    
    def law_of_cosines(self) -> float:
        """Calculate the angle opposite to side c using the law of cosines.\n
        Formula: c^2 = a^2 + b^2 - 2ab * cos(C) => C = cos^-1((a^2 + b^2 - c^2) / (2ab))"""  
        return math.acos((self.side_a ** 2 + self.side_b ** 2 - self.side_c ** 2) / (2 * self.side_a * self.side_b))