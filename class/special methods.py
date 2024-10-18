class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@email.com'

    def fullname(self):
        return self.first+' '+self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # This method is used to format the output of printing a class object
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    # If str method is defined printing a class object will invoke this method
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # will be called when two objects are added
    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee("anil", "nanda", 4000)
emp2 = Employee("ajay", "thekkoote", 5000)


print(emp1)
print(repr(emp1))
print(str(emp1))

print(emp1 + emp2)
