class Student:
  collegeName = "ABC College"
  def __init__(self,name, age):
    self.name = name
    self.age = age
    self.roll = 1
    
  def show(self):
    self.Id = 2
    print(f"Name is {self.name} and age is {self.age}")
    
s1 = Student("Basu", 23)
s1.show()

print(dir(s1))
print(s1.__dict__)
print(help(s1))
# print(help(str))