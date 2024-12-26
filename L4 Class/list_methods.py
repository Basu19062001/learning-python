colors = ["red", "blue", "green"]
print(colors)
colors.append("yellow")
print(colors)
colors.reverse()
print(colors)
colors.sort()
print(colors)

colors.insert(1,"orange")
print(colors)

colors.remove("green")
print(colors)

nums = [2,4,5,7,7,1,36,3,1,324,4]
print(nums)
nums.sort()
print(nums)

nums = [2,4,5,7,7,1,36,3,1,324,4]
print(nums)
nums.sort(reverse=True)
print(nums)

nums = [2,4,5,7,7,1,36,3,1,324,4]
print(nums)
nums.reverse()
print(nums)

nums = [2,4,5,7,7,1,36,3,1,324,4,1,1,1]
print(nums.index(1))
print(nums.index(36))
print(nums.index(324))
print(nums.count(1))

list = ["Basu", "debu"]
temp = list
temp[0] = "Basudev"
print(list)
print(temp)
cars = ["BMW", "Audi", "Benz"]
tempCars = cars.copy()
tempCars[2]="Mercedes"
print(cars)
print(tempCars)

names  = ["Basu","Debu", "Kanan", "Puspa"]
print(names)
names1 = ["Kakali", "Sukla","Rumpa"]
print(names1)
names.extend(names1)
print(names)

string = ["College","School"]
str = ["A","B","C","D"]
print(string + str)