class Employee:

    # this variable is referred using self as the value can be changed by each instance of class
    raise_amount = 1.04

    # this variable is referred by classname as the value remains same for all instances
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('anil', 'nanda', 4000)
emp2 = Employee('ajay', 'thekkoote', 4000)
print(emp1.email)
print(emp1.fullname())

print(emp1.pay)

# changes the variable pay for instance emp1
emp1.apply_raise()

print(emp1.pay)

print(emp2.pay)

# change the value of class variable for the instance emp2
emp2.raise_amount = 1.05
emp2.apply_raise()

print(emp2.pay)

# class variable for emp1 remains same as initial value
print(emp1.raise_amount)
print(emp2.raise_amount)

# referring the class variable with class name
print(Employee.num_of_emps)
