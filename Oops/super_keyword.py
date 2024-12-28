class Parent:
  def __init__(self,name):
    self.name = name
  
  def shows(self):
    print(f"Parent name is {self.name}")
    
class Child(Parent):
  def __init__(self,name,age):
    super().__init__(name)
    self.age = age
  
  def show(self):
    print(f"Child name is {self.name}")
    super().shows()
    
c1 = Child("Basu",23)
c1.show()