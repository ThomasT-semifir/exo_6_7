from person import Person


class Teacher(Person):
    _subject: str = ""

    def __init__(self, age):
        super().__init__(age)

    def explain(self):
        print("Explanation begins")