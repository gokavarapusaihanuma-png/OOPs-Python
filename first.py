class Car:
    def __init__(self,model,color,year,for_sale):
        self.model=model
        self.color=color
        self.year=year
        self.for_sale=for_sale

car1=Car("Mustang","red",2018,False)
car2=Car("Ford","white",2019,True)
car3=Car("BMW","blue",2000,False)
print("Car 1 :")
print(f"{car1.year} {car1.color}  {car1.model}")
print("Car 2 :")
print(f"{car2.year} {car2.color}  {car2.model}")
print("Car 3 :")
print(f"{car3.year} {car3.color}  {car3.model}")


'''
#Class
A class is a blueprint or template used to create objects.
Here, Car is a class that defines what details a car should have.

#Constructor (__init__)
The constructor is a special method that runs automatically when an object is created.
It is used to initialize values like model, color, and year.

#Object
An object is a real instance of a class.
Here, car1, car2, and car3 are objects of the Car class.

#self keyword
self refers to the current object.
It is used to store and access object data.

#Accessing object data
We use object_name.attribute to access values.
Example: car1.year, car1.color.
'''