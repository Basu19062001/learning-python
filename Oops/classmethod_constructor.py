class Student:
  def __init__(self,name, age):
    self.name = name
    self.age = age
  def show(self):
    print(f"Your name is {self.name} and age is {self.age}")

  @classmethod
  def assignValue(cls, string):
    return cls(string.split(",")[0], int( string.split(",")[1] ))

s1 = Student("Basu",23)
s1.show()

string = "Rahul-30"
name = string.split("-")[0]
age = int(string.split("-")[1])
print(name, age)

s2 = Student(name, age)
s2.show()

str1 = "Ziniya,3"
s3 = Student.assignValue(str1)
s3.show()