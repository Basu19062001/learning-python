class Math:
  def __init__(self,a,b):
    self.a= a
    self.b=b
    print(f"You passed {self.a} and {self.b}")
  def addTwoNumber(self,a,b):
    return a+b

  @staticmethod
  def subTwoNumber(a,b):
    return a-b 
  
m = Math(10,20)
print(m.addTwoNumber(25,20))

print(m.subTwoNumber(25,20))
print(Math.subTwoNumber(25,10))