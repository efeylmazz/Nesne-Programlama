class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

if __name__ == "__main__":
    person1 = Person("Hakan Tunc", 46)
    print("Person:")
    person1.display()
    print()

    student1 = Student("Deniz Kaya", 20, "218480")
    print("Student:")
    student1.display()
    print()

    student2 = Student("Kaan Gunay", 21, "263551")
    print("Student:")
    student2.display()
    print()

    teacher1 = Teacher("Yeliz Can", 33, "History")
    print("Teacher:")
    teacher1.display()
    print()
