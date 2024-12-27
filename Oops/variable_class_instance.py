class Employee:
  companyName = "Apple"
  noOfEmp = 0
  def __init__(self,name):
    self.name = name
    self.raise_amount = 0.2
    Employee.noOfEmp += 1
  
  def show(self):
    print(f"The name of employee is {self.name} works in {self.companyName} and the raise amount is {self.raise_amount} and total employees {self.noOfEmp} worked")
    
emp1 = Employee("Basu")
emp1.raise_amount = 0.5
emp1.companyName = "Apple India"
emp1.show() 
Employee.show(emp1) # That's why we pass in method self as a parameter

Employee.companyName = "Facebook"

emp2 = Employee("Rohan")
emp2.raise_amount = 0.3
emp2.show()

emp3 = Employee("Rahul")
emp3.raise_amount = 0.4
emp3.companyName = "Google"
emp3.show()