emp = {143 : 86, 122 : 66, 443 : 80, 48 : 92, 255 : 99 }
print(emp)
print(type(emp))

print(emp.keys())
print(emp.values())

dict = {"name" : "Basudev Samanta"}

emp.update(dict)
print(emp)

dict.clear()
print(dict)

item=emp.pop(48)
print(emp)
print(item)

emp.popitem() # it is used for removing last item of dictionary
print(emp)

del emp # it is used for deleting dictionary
# print(emp) # it will throw an error because of del is deleted the emp dictionary