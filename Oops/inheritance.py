class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id
  def display(self):
    print(f"Name is {self.name} and ID is {self.id}")
    
emp1 = Employee("Basu", 1)
emp1.display()

class Manager(Employee):
  def show(self):
    print("Hello this is Manager class")
    
emp2  = Manager("Rahul", 3)
emp2.display()
emp2.show()

class GrandParent:
  def __init__(self):
    print("I am grand parent")
  def gift(self) -> int:
    return 100

class Parent(GrandParent):
  def __init__(self):
    super().__init__()  
    print("I am parent")
  def gitfOfParent(self) -> int:
    return 1000
class Self(Parent):
  def __init__(self):
    super().__init__()
    print("I am self")
  def myGift(self) -> int:
    return 10000
  
grand = GrandParent()

parent = Parent()
print(parent.gift())
print(parent.gitfOfParent())

me = Self()
print(me.gift())
print(me.gitfOfParent())
print(me.myGift())