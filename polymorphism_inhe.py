'''
Polymorphism = Greek word that means to "have many forms or faces"
            Poly = Many
            Morphe = Form
            TWO WAYS TO ACHIEVE POLYMORPHISM
            1. Inheritance = An object could be treated of the same type as a parent class
            2. "Duck typing" = Object must have necessary attributes/methods
'''

#1 Inheritance
from abc import ABC,abstractmethod

class Shape:
   @abstractmethod
   def area(self):
      pass

class Circle(Shape):
   def __init__(self,radius):
      self.radius = radius
   def area(self):
      return 3.14*self.radius ** 2
class Square(Shape):
   def __init__(self,side):
      self.side = side
   def area(self):
      return self.side ** 2
   
class Triangle(Shape):
    def __init__(self,width,height):
      self.width=width
      self.height=height

    def area(self):
       return 0.5*self.height*self.width
class Pizza(Circle):
   def __init__(self,radius,type):
      super().__init__(radius)
      self.type=type
shapes=[Circle(5),Square(2),Triangle(7,5),Pizza(6,"panner")] #polymorphism

for shape in shapes:
   print(shape.area(),"cm^2")



'''
#Real-Life Analogy:

"Cook" method works differently for different chefs:
Italian Chef.cook() → Makes pasta
Chinese Chef.cook() → Makes noodles
Indian Chef.cook() → Makes curry

Same method name (cook()), different recipes!

#Key Point:

Don't focus on Pizza having its own area() or not
Focus on: All shapes can call .area() even though they calculate it differently
The list [Circle, Square, Triangle, Pizza] treats all as "Shapes" with .area() method

Polymorphism = Treat different objects the same way 
'''
