dict = {
  "name" : "Basudev Samanta",
  "age" : 23,
  "eligible" : True
}

print(dict)
print(dict["name"])
print(dict["age"])
print(dict["eligible"])

print(dict.items())

print(dict.keys())
print(dict.values())

for key in dict.keys():
  print(f"The value of dictionary of key {key} is {dict[key]}" )
  
print()

for val in dict.values():
  print(f"The value of dictionary is {val}" )

print()

for key, value in dict.items():
  print(f"The value of dictionary of key {key} is {value}" )