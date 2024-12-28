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