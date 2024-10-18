# class methods can be used as an alternative to create objects. class methods can be use as multiple ways of creating an object

import datetime


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    # a function which takes instance as first argument is the regular method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # a class method takes first argument as class and defined using the decorator
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, inp):
        first, last, pay = inp.split('-')
        return cls(first, last, pay)

    # static methods doesn't have a class or instance as an argument, they are normal python function.
    # If a function doesn't refer and instance or class anywhere within the function, define it as statuc method.
    @staticmethod
    def is_wokday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('anil', 'nanda', 5000)
emp_2 = Employee('ajay', 'thekkoote', 6000)

print(emp_1.fullname())

print(emp_1.raise_amt)

# sets the raise amount variable in class to 1.05
Employee.set_raise_amount(1.05)

print(emp_2.raise_amt)


# using class methods to create objects
emp_str_3 = 'john-make-1000'

emp_3 = Employee.from_string(emp_str_3)

print(emp_3.fullname())

my_date = datetime.date(2024, 10, 18)

print(Employee.is_wokday(my_date))
