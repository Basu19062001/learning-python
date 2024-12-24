names = "Basudev"
print(len(names))

# Slicing
str = "Basudev"

print(str[0:5])
print(str[:5]) # by default 0
print(str[1:5])
print(str[:]) # by default -> 0 : len(str)
print(str[0:])
print(str[1:])
print(str[0:-2]) # this means -> [0 : len(str) - 2] here [0:(7-2)] = [0:5]

print(str[:len(str)-5])
print(str[-2: 5])
print(str[-2:3])
print(str[-6:-2])