i = int(input("Enter any number : "))

while(i<=10):
  print(i, end=" ")
  i += 1
print("\nEnd of loop")

count = int(input("Enter any number : "))
while(count>0):
  print(count, end=" ")
  count -= 1

no = int(input("\nEnter any number : "))
while(no<50):
  print(no, end=" ")
  no += 3
else:
  print("\nInside of else")
  
  
  
# Do while 
count = 0
while(True):
  print("Hello", end=" ")
  count += 1
  if(count == 20):
    break
else:
  print("Loop breaked : ",count)
print("\nOutside the loop | Count : ",count)