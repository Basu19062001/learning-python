marks = [23, 55, 65, 21, 98, 2, 44, 89]

index = 0 
for mark in marks:
  print( mark)
  if(index == 4):
    print("Awesome Mark")
  index += 1
  
marks = [34, 67, 98, 76, 99, 21, 54, 65, 55]

index = 0
for index, mark in enumerate(marks):
  print(mark)
  if(index == 5):
    print("Don't worry you can do it")
  index += 1

animals = ["Dog", "Cat", "Lion", "Tiger", "Elephant", "Rabbit"]

for index, animal in enumerate(animals, start=1):
  print(f"index = {index}, animal = {animal}")