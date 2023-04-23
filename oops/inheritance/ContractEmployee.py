from oops.inheritance.Employee import Employee


class ContractEmployee(Employee):

    def __init__(self, name, id, organisation, designation, contractVendor):
        super(ContractEmployee, self).__init__(name, id, organisation, designation)
        self.contractVendor = contractVendor

    def printDetails(self):
        print("My name is  ", self.name)
        print("My id is: ", self.id)
        print("My organisation is  ", self.organisation)
        print("My designation is: ", self.designation)
        print("My work through agency : ", self.contractVendor)
