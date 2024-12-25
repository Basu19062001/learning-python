age = int(input("Enter you age : "))

match age:
  case _ if age < 4:
    print("You are in Infancy")
  case _ if age >4 and age <= 12:
    print("You are in Childhood")
  case _ if age > 12 and age <= 19:
    print("You are in Teenage")
  case _ if age > 19 and age <= 35:
    print("You are in Adult")
  case _ if age > 35 and age <= 60:
    print("You are in Middle Age")
  case _:
    print("You are in Senescence")