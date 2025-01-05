class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old


    # @property
    # def name(self):
    #     return self.__name
    #
    #
    # @name.setter
    # def name(self, name):
    #     self.__name = name


    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


p = Person('Sergey', 20)

p.old = 35

print(p.old, p.__dict__, p._Person__name)