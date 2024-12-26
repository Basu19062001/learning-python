list = [1,2,34,5,6,7]
list2 = [1,"Basu", True, 2.5, None, 5+6j]
print(list)
print(list2)
print(type(list))
print(type(list2))

colors = ["red", "Green", "Blue", "Yellow"]
print(colors)

print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

numbers = [1,2,4,5,7,8,9,2,21,34,4,577,8]
print(numbers[:])
print(numbers[:len(numbers)])
print(numbers[0:])
print(numbers[0:len(numbers)])

print("length :",len(numbers))
print(numbers[-1])
print(numbers[len(numbers)-1])
# print(numbers[len(numbers)]) # Throws an error
print(numbers[:-4])
print(numbers[-7:-3])
print(numbers[::2])
print(numbers[:7:2])

animals = ["Cat", "Dog", "Elephant", "Tiger", "Lion", "Monkey"]
print(animals)
print(animals[:])
print(animals[:len(animals)])
print(animals[-6:-1])
print(animals[::2])
for animal in animals:
  print(animal, end=" ")

print("\n")
i = 0
while(i<len(animals)):
  print(animals[i], end=" ")
  i += 1
  
print("\n")
if "Dog" in animals :
  print("yes")
else:
  print("No")

if "Crocodile" in animals :
  print("yes")
else:
  print("No")
  
  
# in operator is use in string as well
name = "Basudev"
if "su" in name:
  print("yes")
else:
  print("No")
  
if "dec" in name:
  print("yes")
else:
  print("No")
  
# List Comprehension 
nums = [i for i in range(1,11)]
print(nums)

nums = [i*i for i in range(1,11) if i%2==0]
print(nums)
for num in nums:
  print(num, end=" ")
print("\n")

names = ["Basu","Debu","Kanan","Puspa","Kakali","Sukla","Rumpa"]
print(names)
retainNames = [name for name in names if "s" in name]
print(retainNames)
namesWith = [name for name in names if len(name)>5]
print(namesWith)