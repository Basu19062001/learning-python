a = input("Enter the number: ")
print(f"Multiplication table of {a} is :")

try:
  for i in range(1,11):
    print(f"{int(a)} x  {i} = {int(a)*i}")
except Exception as e:
  print(e)

print("This is imp line of the code... must be execute")
print("End of loop")

try:
  num = int(input("Enter any number:"))
  a = ["Basu", "Python Developer"]
  print(a[num])
except ValueError:
  print("Invalid Input")
except IndexError:
  print("Index error")
finally:
  print("This is the finally block")