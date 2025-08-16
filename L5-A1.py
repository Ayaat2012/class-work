# Parent class
class Person():

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ ofr the parent class
        Person.__init__(self, name, idnumber)


# Creation of an object variable or an instance
a = Employee('Penguin', 20130613, 15000, "Intern")

# CAlling a function of the class Person using its instance
a.display()