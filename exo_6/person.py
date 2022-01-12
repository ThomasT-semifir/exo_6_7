class Person(object):
    _age: int = 0
    def __init__(self, age):
        self._age = age

    def say_hello(self):
        print("Hello!")

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        self._age = value