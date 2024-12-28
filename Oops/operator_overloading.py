class Vector:
  """
  Represents a 3D vector with components i, j, and k.

  Attributes:
    i (int or float): The i-component of the vector.
    j (int or float): The j-component of the vector.
    k (int or float): The k-component of the vector.

  Methods:
    __init__(i, j, k): Initializes a new Vector instance.
    __str__(): Returns a string representation of the vector.
    __add__(x): Returns the sum of this vector and another vector x.
  """
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k
    
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  
  def __add__(self, x):
    return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
  
  def __call__(self):
    print("""
  Represents a 3D vector with components i, j, and k.

  Attributes:
    i (int or float): The i-component of the vector.
    j (int or float): The j-component of the vector.
    k (int or float): The k-component of the vector.

  Methods:
    __init__(i, j, k): Initializes a new Vector instance.
    __str__(): Returns a string representation of the vector.
    __add__(x): Returns the sum of this vector and another vector x.
  """)
  
v1 = Vector(1,2,3)
print(v1)
v2 = Vector(4,5,6)
print(v2)
print(v1 + v2)
print(type(v1 + v2))
print(v1.__doc__)

v1()
