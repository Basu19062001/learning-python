nums = {1,2,3,2,1,2,4,67,32,2,12,1}
print(nums)
print(type(nums))

collection  ={"basu", 12,23, 5,True, None, 5,5.2}
print(collection)
print(type(collection))

for item in collection:
  print(item, end=" ")
print("\n")

empty = {} # this is a empty dictionary
print(type(empty))

empty = set() # this is a empty set
print(type(empty))
print(dir(empty))