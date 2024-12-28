class Animal:
  def __init__(self, name, spices):
    self.name = name
    self.spices = spices
  
  def __str__(self):
    return f"Name is {self.name} and spices are {self.spices}"
  
  def makeSound(self):
    print("Animal sound")
    
class Dog(Animal):
  def __init__(self, name, breed):
    self.name  = name
    self. breed = breed
  
  def __str__(self):
    return f"Name is {self.name} and breed is {self.breed}"
  
  def sound(self):
    print("Bark Bark")
    
d = Dog("Igirs", "German Shepherd")
print(d)
d.sound()
d.makeSound()

a = Animal("Cat", "Persian")
print(a)
a.makeSound()