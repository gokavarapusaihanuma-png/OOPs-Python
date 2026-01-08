'''
super() = Calls parent class methods
Used in child classes to access parent functionality
'''

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def description(self):
        print("Parent shape description")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # Calls Shape.__init__
        self.radius = radius
    
    def description(self):
        print("Child circle description")  # ⭐ Overrides completely (no super)

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled) 
        self.side = side
    
    def description(self):
        super().description()  # ⭐ Calls parent method only

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled) 
        self.width = width
        self.height = height
    
    def description(self):
        super().description()  # ⭐ Calls parent method
        print("And child triangle description")  # ⭐ Adds own functionality

# Testing three different description() approaches:
circle = Circle("red", True, 5)
print(f"Circles's color is {circle.color} and it's  {'filled' if circle.is_filled else 'not filled'}")
print(f"Area: {3.14*circle.radius*circle.radius} cm^2")
circle.description()  # Output: "Child circle description" (overrides completely)

square = Square("blue", False, 6)
print(f"\nSquare's color is {square.color} and it's  {'filled' if square.is_filled else 'not filled'}")
print(f"Area: {square.side*square.side} cm^2")
square.description()  # Output: "Parent shape description" (uses parent only)

triangle = Triangle("Green", False, 4, 9)
print(f"\nTriangle's color is {triangle.color} and it's  {'filled' if triangle.is_filled else 'not filled'}")
print(f"Area: {0.5*triangle.height*triangle.width} cm^2")
triangle.description()  # Output: "Parent shape description" + "And child triangle description" (extends)