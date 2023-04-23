from oops.inheritance.Person import Person


class Student(Person):

    def __init__(self, name, id, college, course, yearOfPassing):
        super(Student, self).__init__(id, name)
        self.college = college
        self.course = course
        self.yearOfPassing = yearOfPassing

    def printDetails(self):
        print("My name is  ", self.name)
        print("My id is: ", self.id)
        print("My college is  ", self.college)
        print("My course is  ", self.course)
        print("My yearOfPassing is: ", self.yearOfPassing)
