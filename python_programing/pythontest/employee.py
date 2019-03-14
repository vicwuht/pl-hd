class Employee():
    def __init__(self, lastname, firstname, salary):
        self.lastname = lastname
        self.firstname = firstname
        self.salary = salary
    def give_raise(self, salary_raise=5000):
        self.salary += salary_raise


