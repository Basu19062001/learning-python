for i in range(1,101):
  if(i%2==0):
    continue
  print(i, end=" ")
  if(i%25==0):
    break   
print("\n")
for i in range(1,12):
  print("5 x",i," = ",5*i)
  if(i==10):
    break