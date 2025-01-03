# # Encapsulation

# class BankAccount:
#   def __init__(self, name, account_number, balance):
#     self.__name = name
#     self.__account_number = account_number
#     self.__balance = balance
  
#   def deposit(self, amount):
#     self.__balance += amount
#     print(f"Deposited successfully\n Deposit amount : {amount}")
    
#   def withdraw(self, amount):
#     if(self.__balance >= amount):
#       self.__balance -= amount
#       print(f"Withdrawal successful\n Withdrawal amount {amount}")
#     else:
#       print("Insufficient balance")
  
#   def get_account_info(self):
#     masked_account_number = "********" + self.__account_number[-4:]
#     print(f"Name: {self.__name}\nAccount Number: {masked_account_number}\nBalance: {self.__balance}")
  
  
# acc = BankAccount("Rohan", "125487963258", 1000)
# acc.get_account_info()
# acc.deposit(1500)
# acc.get_account_info()
# acc.withdraw(2000)
# acc.get_account_info()
# acc.withdraw(5000)

# print(acc._BankAccount__account_number)



# Abstraction
# from abc import ABC, abstractmethod

# class Shape(ABC):
  
#   @abstractmethod
#   def area(self):
#     pass

#   @abstractmethod 
#   def perimeter(self):
#     pass

# class Rectangle(Shape):
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width
    
#   def area(self):
#     return self.length * self.width
  
  
#   def perimeter(self):
#     return 2*(self.length + self.width)
  

# rect = Rectangle(10, 5)
# print(rect.area())
# print(rect.perimeter())



# Polymorphism
# class Shape:
#   def __init__(self,x,y):
#     self.x = x
#     self.y = y
    
#   def area(self):
#     return self.x * self.y
  
# class Circle(Shape):
#   def __init__(self, radius ):
#     super().__init__(radius, radius)
  
#   def area(self):
#     return 3.14 * super().area()
  
  
  
# circle = Circle(5)
# print(circle.area())

# class Bird:
#   def speak(self):
#     print("Bird is chirping")
    
# class Dog:
#   def speak(self):
#     print("Dog is barking")

# def make_sound(animal):
#   animal.speak()    

# sparrow = Bird()
# goldenRetriever = Dog()

# make_sound(sparrow)
# make_sound(goldenRetriever)




# Inheritance

# # single inheritance
# class Vehicle:
#   def __init__(self, brand, model ):
#     self.brand = brand
#     self.model = model
  
#   def start(self):
#     print(f"The {self.brand} {self.model} is starting")
    
#   def stop(self):
#     print(f"The {self.brand} {self.model} is stopping")
    
# class Car(Vehicle):
#   def __init__(self, brand, model, doors):
#     super().__init__(brand, model)
#     self.doors = doors
    
    
#   def honk(self):
#     print("Beep Beep!")


# my_car = Car("Honda", "Civic", 4)
# my_car.start()
# my_car.honk()
# my_car.stop()

# # Multiple Inheritance
# class Father:
#   def skills(self):
#     print("Father has good thinking skills.")
    
# class Mother:
#   def skills(self):
#     print("Mother has good decision making skills.")
    
# class Me(Father, Mother):
#   def additional_skills(self):
#     print("Me has learning programming skills.")
    
# child = Me()
# child.skills()
# child.additional_skills()

# # Multilevel Inheritance

# class Vehicle:
#   def start(self):
#     print("The vehicle is starting.")
    
# class Car(Vehicle):
#   def drive(self):
#     print("The car is begin driving.")
    
# class SportCar(Car):
#   def race(self):
#     print("The sports car is racing.")
    
# sports_car = SportCar()
# sports_car.start()
# sports_car.drive()
# sports_car.race()

# # Hierarchical Inheritance

# class Shape:
#   def area(self):
#     print("Calculating area...")
    
# class Rectangle(Shape):
#   def rectangle_area(self, length, breadth):
#     return length * breadth

# class Circle(Shape):
#   def circle_area(self, radius):
#     return 3.14 * radius  * radius
  
# rect = Rectangle()
# rect.area()
# print(f"Rectangle area: {rect.rectangle_area(10, 5)}")

# circle = Circle()
# circle.area()
# print("Circle area: ", circle.circle_area(5))

# # Hybrid Inheritance

# class Engine:
#   def engine_type(self):
#     print("This is a petrol engined.")
    
# class Vehicle:
#   def vehicle_type(self):
#     print("This is a four wheeler.")
    
# class Car(Engine, Vehicle):
#   def car_type(self):
#     print("This car brand is Honda.")
    
# car = Car()
# car.engine_type()
# car.vehicle_type()
# car.car_type()



# Practice
