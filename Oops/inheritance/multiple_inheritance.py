class MyDad:
  def __init__(self, name , age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"Dad name is {self.name}"
  
  def efficiencyDad(self):
    print("Good Decision Maker")
  
  def show(self):
    print(f"Dad's method")

class MyMom:
  def __init__(self, name , age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"Mom name is {self.name}"
  
  def efficiencyMom(self):
    print("Good Thinker")
  
  def show(self):
    print(f"Mom's method")
    
class Me(MyDad, MyMom ):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"My name is {self.name}"
  
  def efficiencyMe(self):
    print("Good Learner")

me = Me("Basudev", 23)
me.efficiencyDad()
me.efficiencyMom()
me.efficiencyMe()
print(me)
me.show()
print(Me.mro())