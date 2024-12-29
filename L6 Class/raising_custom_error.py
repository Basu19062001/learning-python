num = int(input("Enter a number : "))

if(num < 5 or num > 9):
  raise ValueError("Enter number between 5 to 9")
else:
  print("Good")

