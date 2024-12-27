#Default constructor
class Person:
  def __init__(self):
    print("Hey! I am a person")
    
a = Person()

class Person:
  def __init__(self,name,occupation):
    print("Hello!")
    self.name = name
    self.occupation = occupation
  def info(self):
    print(f"{self.name} is a {self.occupation}") 

a = Person("Basu","Software Developer")
a.info()

b=Person("Kakali","CEO")
b.info()