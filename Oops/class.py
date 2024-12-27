class Person:
  name = "Basu"
  occupation = "Software Developer"
  networth = "$10M"
  
  def info(self):
    print(f"{self.name} is a {self.occupation} with net worth {self.networth}")
  

a = Person() # creating an object
a.name = "Debesh"
a.occupation = "Programmer"
a.networth  = "$20M"
a.info()

b = Person()
b.name = "Kakali"
b.occupation="CEO"
b.networth = "$10M"
b.info()

c = Person()
c.info()