# String format
name = "Basudev"
country = "India"
letter = "Hey! my name is {1} and I am from {0}"

letter = letter.format(country, name)
print(letter)

# f-string

name = "Basudev"
country = "India"
print(f"Hey my name is {name} and I am from {country}")
print("Hey my name is",name,"and I am from",country)

print(f"f-string format is like -> Hey! my name is {{name}} and I am from {{country}}")

price  = 4.069568866
print(f"Price is {price} dollars!")
print(f"Price is {price: .2f} dollars!")

print(type(f"{2 * 50}"))