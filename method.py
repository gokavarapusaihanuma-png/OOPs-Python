class Car:
    def __init__(self,model,color,year,for_sale):
        self.model=model
        self.color=color
        self.year=year
        self.for_sale=for_sale

    def drive(self):
        print(f"You are driving {self.model}")

    def stop(self):
        print(f"You stopped driving {self.model}")

car1=Car("Mustang","red",2018,False)
car2=Car("Ford","white",2019,True)


car1.drive()
car1.stop()
car2.drive()
car2.stop()

'''
#Class
Car is a class that represents a car.

Constructor (__init__)
It is used to assign values to a car when an object is created.

#Methods

drive() → shows driving action

stop() → shows stopping action

#Object
car1 and car2 are objects created from the Car class.

#Method calling
Methods are called using the object name.
Example: car1.drive()


'''
