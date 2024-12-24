str = "Basu"
print(len(str))
print(str)

str = "!!!Bausdev !!!!"
print(str.upper())
print(str.lower())

str = "!!!Basudev!!!!!!!!!"
print(str.rstrip("!"))
str =  "!!Basu!! !!Basu!!!!!!!!!!!!!"
print(str.rstrip("!"))

str =  "!!!Basu !!! Basu !!!!! hi !!! Basu"
print(str.replace("Basu","Basudev"))

str = "Basu is become a programmer ASAP"
print(str.split(" "))

str = "introduction of myself"
print(str.capitalize())
str = "hey My name is Basu do yOu KnOw that I am Became a Programmer"
print(str.capitalize())

str = "Quester"
print(str.center(20))
print(len(str))
print(len(str.center(20)))
print(str.center(50,"*"))

str = "Basudev samanta  hi I am basu, basu is basu"
print(str.count("a"))
print(str.count("basu"))

str = "This is a beautiful day"
print(str.endswith("day"))
str = "This is a beautiful day !!"
print(str.endswith("day"))

str = "ThisIsAString"
print(str.isalnum())
str = "ThisIsAString234"
print(str.isalnum())
str = "ThisIsAString!@#$%"
print(str.isalnum())
str = "Thisisastring"
print(str.isalnum())

str = "Alphabet"
print(str.isalpha())
str = "alphabet"
print(str.isalpha())
str = "alphabet123"
print(str.isalpha())

str = "Hi there How are you"
print(str.isprintable())
str = "Hi there How are you\n"
print(str.isprintable())

str = "            " # using spacebar
print(str.isspace())
str = " " # using Tab
print(str.isspace())
str= "Basu "
print(str.isspace())
str= "   Basu "
print(str.isspace())

str = "Welcome To Python"
print(str.istitle())
str = "welcome to blackzone"
print(str.istitle())
print(str.title())

str  =  "Basu is ..."
print(str.startswith("Basu"))
print(str.startswith("basu"))

str = "Hi This side Basu"
print(str.swapcase())
