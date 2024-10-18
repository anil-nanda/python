class test:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def double_age(self):
        return self.age*2


anil = test("anil", 22)
sid = test("sid", 32)

print(anil.age)

print(anil.double_age())
