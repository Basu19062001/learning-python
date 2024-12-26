#Default Arguments
#Required Arguments
#Keyword Arguments
#Variable length Arguments

#Default Arguments
def addTwoNumber(a=1,b=1):
  print(a+b)
  
addTwoNumber()
addTwoNumber(5)
addTwoNumber(b=10)
addTwoNumber(a=10,b=5)
  
#Required Arguments
def findGreaterBtwTwoNumber(a,b):
  if(a>b):
    print(a," is greater than ",b)
  elif(b>a):
    print(b," is greater than ",a)
  else:
    print("Both are equal")

findGreaterBtwTwoNumber(10,20)
findGreaterBtwTwoNumber(202,54)
findGreaterBtwTwoNumber(20,20)
# findGreaterBtwTwoNumber() We can't do this

#Variable length Arguments
def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum += i
  return sum/len(numbers)

avg = average(1,2,3,4,4,5,6,6,7)
print(avg)

#Keyword Arguments
def printName(**name):
  print(type(name))
  print("Hello!", name["fname"], name["mname"], name["lname"])
  
printName(fname="Bsaudev",mname="",lname="Samanta")