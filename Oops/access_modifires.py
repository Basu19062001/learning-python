# public access modifier
# private access modifier
# protected access modifier

# public access modifier
class Student:
  def __init__(self, name, age):
    self.name = name # public variable
    self.age = age # public variable
  def info(self):
    print(f"Name is {self.name} and age is {self.age}")
    
a = Student("Basu", 23)
print(a.name)
print(a.age)
a.info()



# private access modifier
class Employee:
  def __init__(self,name, age):
    self.__name = name # private variable
    self.__age = age
  def __showData(self):
    print(f"Name is {self.__name} and age is {self.__age}")
    
class Programmer(Employee):
  pass

emp = Employee("Basu",23) 
# emp.__showData() # It will throws an error because of private
# print(emp.__name) # It will throws an error because of private
# print(emp.__age) # It will throws an error because of private

emp2 = Programmer("Empty", 23)
# emp2.__showData() # It will throws an error because of private
# print(emp2.__name) # It will throws an error because of private
# print(emp2.__age) # It will throws an error because of private

# we can access the private variable indirectly
print(emp._Employee__name)
print(emp._Employee__age)
emp._Employee__showData()

# This is called name mangling
print(emp2._Employee__name)
print(emp2._Employee__age)
emp2._Employee__showData()
print(dir(emp))


# protected access modifier
class Random:
  def __init__(self, name):
    self._name = name # protected variable
  
  def _display(self): # protected method
    print(f"Name is {self._name}")

class Random2(Random):
  pass

obj = Random("basu")
print(obj._name)
obj._display()

obj2 = Random2("Rahul")
obj2._display()
print(obj2._name)