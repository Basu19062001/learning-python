class DataStoreAndGet:
  def __init__(self, value):
    self.__value = value
  def showData(self):
    print(f"Value is {self.__value}")

  @property  # used for getter
  def value(self) -> int:
    return self.__value
  
  @value.setter
  def value(self,new_value: int):
    '''Sets the value of the private attribute.

This method is a setter for the value attribute, allowing controlled modification of the private __value attribute. It enables encapsulation by providing a way to set the value with potential validation or additional logic.

Args:
    new_value (int): The new value to be assigned to the private attribute.
'''
    self.__value = new_value
  

a = DataStoreAndGet(10)
a.showData()

print(a.value)
a.value = 20
a.showData()

print(a.value)