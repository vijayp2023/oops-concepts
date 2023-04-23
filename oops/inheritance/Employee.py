from oops.inheritance.Person import Person


class Employee(Person):
    def __init__(self, name, id, organisation, designation):
        super(Employee, self).__init__(name, id)
        self.organisation = organisation
        self.designation = designation

    def printDetails(self):
        print("My name is  ", self.name)
        print("My id is: ", self.id)
        print("My organisation is  ", self.organisation)
        print("My designation is: ", self.designation)
