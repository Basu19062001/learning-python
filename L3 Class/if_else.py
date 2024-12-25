# If else

age = int(input("Enter your age :"))

if(age >= 18):
  print("You can vote")
else:
  print("You can't vote")

#If else ladder

age = int(input("Enter your age : "))

if(age >= 18):
  print("You can drive")
elif(age >= 60 and age<= 70):
  print("You can't drive, you need help")
else:
  print("You can't drive")
  
# Nested if else

no = int(input("Enter any number :"))

if(no % 2 == 0):
  if(no % 4 == 0):
    print("Number is divisible by 4")
  else:
    print("Number is not divisible by 4")
else:
  if(no % 5 == 0):
    print("Number is divisible by 5")
  else:
    print("Number is not divisible by 5")