class Employee:
  company = "Apple"
  def __init__(self, name):
    self.name  = name
  
  def show(self):
    print("The Employee is ", self.name, " works in ", self.company)
    
  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany  
    
emp = Employee("basu")
emp.show()
emp.company = "Google"
emp.show()
print(Employee.company)
emp.show()

Employee.changeCompany("Facebook")
print(Employee.company)
emp.changeCompany = "Microsoft"
emp.show()
print(Employee.company)