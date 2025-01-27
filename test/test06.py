class Person:

    def __init__(self, name: str = None, age: int = None, city: str = None):
        self.name = name
        self.age = age
        self.city = city


a = Person('Anton', 30, 'Kiev')
a2 = Person()
