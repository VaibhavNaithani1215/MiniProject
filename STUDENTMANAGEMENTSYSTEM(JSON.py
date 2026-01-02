import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"The name of Student is {self.name} and marks is: {self.marks}")


def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_student_json():
    students = load_students()

    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    s = Student(name, marks)

    student_data = {
        "name": s.name,
        "marks": s.marks
    }

    students.append(student_data)

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def view_students():
    students = load_students()

    if not students:
        print("No students found!")
    else:
        for student in students:
            s = Student(student["name"], student["marks"])
            s.display()


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        break
    elif choice == 1:
        save_student_json()
    elif choice == 2:
        view_students()
    else:
        print("Invalid choice")
