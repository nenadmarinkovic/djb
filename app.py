class Person:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def fullname(self):
        return "{} {}".format(self.first, self.last)


e_1 = Person('Nenad', 'Marinkovic', 'n@n.com')
e_2 = Person('Helena', 'Hagauer', 'h@h.com')
e_3 = Person('Ix', 'Alth', 'h@h.com')


print(Person.fullname(e_1))