def calculateGeomatryMeans(a,b):
  mean = (a*b)/(a+b)
  print("Geomatry mean of ",a," and ",b," is ",mean)


def greaterOfTwoNumber(a,b):
  if(a>b):
    print("First number is grater")
  elif(b>a):
    print("Second number is greater than first number")
  else:
    print("Both are qual numbers")

def averageOfTwoNumber(a,b):
  pass

a = int(input("Enter first number for calculate geomatry means:"))
b = int(input("Enter first number for calculate geomatry means:"))
calculateGeomatryMeans(a,b)

print("Enter Two Numbers : \n")
x = int(input())
y = int(input())
greaterOfTwoNumber(x,y)