class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def fullname(self):
        return self.first+' '+self.last


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Can also be initialized like Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addemp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def removeemp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def printemp(self):
        for employee in self.employees:
            print(employee.fullname())


emp1 = Developer('anil', 'nanda', 6000, 'Python')
emp2 = Employee('ajay', 'thekkoote', 6000)

# help on a class in python
# print(help(Developer))

print(emp1.email)
print(emp1.prog_lang)

print(emp1.pay)

# This uses raise_amount from Developer class
emp1.apply_raise()

# This uses raise_amount from Employee class
emp2.apply_raise()

print(emp1.pay)
print(emp2.pay)


mgr1 = Manager("su", "nu", 7000, [emp1])

print(mgr1.email)

mgr1.addemp(emp2)

mgr1.printemp()

mgr1.addemp(emp1)

mgr1.printemp()
