from oops.inheritance.ContractEmployee import ContractEmployee
from oops.inheritance.Employee import Employee
from oops.inheritance.PermanentEmployee import PermanentEmployee
from oops.inheritance.Person import Person
from oops.inheritance.Student import Student

print("_____________ Person Start ___________________")
vijay = Person("Vijay", 23213)
balaji = Person("Balaji", 90099)
vijay.printDetails()
balaji.printDetails()
print("______________ Person  End __________________")

print("................ Employee Start .............................................")
vijay_Employee = Employee("Vijay", 3123, "TCS", "Software Engineer")
balaji_Employee = Employee("Balaji", 32123, "Mindtree", "Software Architect")
vijay_Employee.printDetails()
print("________________________________")
balaji_Employee.printDetails()
print("..................Employee End.........................................")

print("..................PermanentEmployee start.........................................")
vijay_PermanentEmployee = PermanentEmployee("vijay", 3123, "TCS", "Software Engineer", 10000)
balaji_PermanentEmployee = PermanentEmployee("balaji", 32123, "mindtree", "Software architect", 30000)
vijay_PermanentEmployee.printDetails()
balaji_PermanentEmployee.printDetails()

print("..................PermanentEmployee END.........................................")

print("..................ContractEmployee  start.........................................")

vijay_contractEmployee = ContractEmployee("vijay", 3123, "TCS", "Software Engineer", "Palle Consultancy")
balaji_contractEmployee = ContractEmployee("balajii", 3123, "TCS", "Software Engineer", "Moorthi Manpower Agency")
vijay_contractEmployee.printDetails()
balaji_contractEmployee.printDetails()

print("..................ContractEmployee End.........................................")

print("..................Student Start.........................................")
vijay_student = Student("vijay", 3123, "nandha arts and science college", "computer science", 2022)
balaji_student = Student("balaji", 32123, "nandha engineer college", "mechanical engineering", 1990)
vijay_student.printDetails()
balaji_student.printDetails()
print("..................Student End.........................................")

