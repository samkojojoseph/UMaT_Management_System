class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def display(self):
        print("My name is", self.name)
        print(f"I am {self.age} years old")


# ================= Student Details =================
print("\n=== Student Details ===")

class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = input("Enter your student ID: ")
        self.enroll_course = input("Enter your enrolled course: ")

    def sam(self):
        print("Student ID:", self.student_id)
        print("Enrolled Course:", self.enroll_course)


joseph = Student()
joseph.display()
joseph.sam()


# ================= Lecturer Details =================
print("\n=== Lecturer Details ===")

class Lecturer(Person):
    def __init__(self):
        super().__init__()
        self.employee_id = input("Enter your employee ID: ")
        self.teach_course = input("Enter your teaching course: ")

    def kojo(self):
        print("Lecturer ID:", self.employee_id)
        print("Teaching Course:", self.teach_course)


lecturer = Lecturer()
lecturer.display()
lecturer.kojo()