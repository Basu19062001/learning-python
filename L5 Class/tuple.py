tup = (11,2,34,4,6,6,3)
print(type(tup), tup)

tup = ("Hello", 1,2,4,6,12,45, True, None)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
# tup[0] = 1 # we can't change tuple because of immutability

print(tup[:])
print(tup[:-1])
# print(tup.reverse())

tup2 = tup[1:8]
print(tup2)

tup = ("Red", "Blue", "Green","Yellow")
for color in tup:
  print(color,end=" ")
print("\n")  
  
if "Cyan" in tup:
  print("Yes")
else:
  print("No")


for color in tup:
  print(color)
  for c in color:
    print(c)   

empty = (1) # this is a int
print(type(empty))

empty = (1,) # this is a tuple
print(type(empty))

# empty = [] # this is a list
# print(type(empty))