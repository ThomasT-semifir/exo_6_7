from person import Person


class Student(Person):
    def __init__(self, age):
        super().__init__(age)

    def go_to_classes(self):
        print("I'm going to class")

    def display_age(self):
        print(f"Mon âge est {self.age}")