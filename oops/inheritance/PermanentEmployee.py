from oops.inheritance.Employee import Employee


class PermanentEmployee(Employee):

    def __init__(self, name, id, organisation, designation, pfNumber):
        super(PermanentEmployee, self).__init__(id, name, organisation, designation)
        self.pfNumber = pfNumber

    def printDetails(self):
        print("My name is  ", self.name)
        print("My id is: ", self.id)
        print("My organisation is  ", self.organisation)
        print("My designation is: ", self.designation)
        print("My pfNumber is: ", self.pfNumber)
