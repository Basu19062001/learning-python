#Joining set methods
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities3 = cities1.union(cities2)
print(cities3)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities1.update(cities2)
print(cities1)




cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities3 = cities1.intersection(cities2)
print(cities3)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities1.intersection_update(cities2)
print(cities1)





cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities1.symmetric_difference_update(cities2)
print(cities1)




cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities3 = cities1.difference(cities2)
print(cities3)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
cities1.difference_update(cities2)
print(cities1)


# Setting set methods

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
print(cities1.isdisjoint(cities2))

cities1 = {""}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
print(cities1.isdisjoint(cities2))



cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Kolkata", "Berlin", "Hyderabad"}
print(cities1.issuperset(cities2))
cities3 = {"Madrid", "Delhi"}
print(cities1.issuperset(cities3))



cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Kolkata", "Tokyo", "Delhi"}
print(cities2.issubset(cities1))
cities3 = {"Berlin", "Delhi"}
print(cities3.issubset(cities1))


cities1= {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities1.add("Kolkata")
print(cities1)



cities1 = {"Tokyo","Madrid","Berlin", "Delhi"}
cities2 = {"Madrid", "Delhi", "Kolkata"}
cities1.update(cities2)
print(cities1)


cities1 = {"Tokyo", "Mardrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Kolkata", "Hyderabad"}
cities1.update(cities2)
print(cities1)
cities1.remove("Tokyo")
print(cities1)
cities1.discard("Delhi")
print(cities1)


cities1 = {"Tokyo", "Mardrid", "Berlin", "Delhi"}
item = cities1.pop()
print(item)
print(cities1)


cities1 = {"Tokyo", "Mardrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Kolkata", "Hyderabad"}
cities1.clear()
print(cities1)
print(cities2)

del cities2 # set is deleted
# print(cities2)