class Employee:
  def __init__(self,name):
    self.name = name
    
  def show(self):
    print(f"The name of employee is {self.name}")
  
  def __len__(self):
    i=0
    for ch in self.name:  
      i += 1
    return i
    
e1 = Employee("Basudev Samanta")
e1.show()
print(len(e1))
print(e1)

class Student:
  def __init__(self,name):
    self.name = name
  
  def show(self):
    print(f"The name of the Student is {self.name}")
  
  def __str__(self):
    return f"This is the Student class and Student name is {self.name} str method"
  
  def __repr__(self):
    return f"This is the Student class and Student name is {self.name} repr method"
  
  def __call__(self):
    print( """
  Represents a student with a name.

  Attributes:
    name (str): The name of the student.

  Methods:
    show(): Prints the name of the student.
    __str__(): Returns a string representation of the student.
    __repr__(): Returns a string representation of the student for debugging purposes.
  """)
  
s1 = Student("Basudev Samanta")
s1.show()
print(s1)
s1()

