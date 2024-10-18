class Employee:

    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # email attribute won't change if the first of an object is changed, for that we define email as method with @property decorator
        # self.email = first+'.'+last+'@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return self.first+' '+self.last

    # email is made with first and last names, changing the email address can change the first and last using a setter method like below
    @email.setter
    def email(self, email):
        name = email.split('@')[0]
        first, last = name.split('.')
        self.first = first
        self.last = last

    @email.deleter
    def email(self):
        print("delete name")
        self.first = None
        self.last = None


emp1 = Employee("anil", "nanda")
emp2 = Employee("ajay", "thekkoote")

emp1.email = 'jo.we@email.com'

print(emp1.fullname())

del emp1.email

print(emp1.fullname())
