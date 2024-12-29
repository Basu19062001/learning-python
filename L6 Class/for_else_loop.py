for i in range(10):
  print(i+1, end=" ")
  
else:
  print("\nThis is else section of loop")
  
for i in range(5):
  print(i+1, end=" ")
  if i==3:
    break
else:
  print("\nelse section")