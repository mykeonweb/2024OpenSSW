# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def calculate_average(self):
        return (self.korean + self.english + self.math) / 3


def main():
    num_students = int(input("Enter the number of students: "))
    students = []

    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        korean = float(input("Enter Korean score: "))
        english = float(input("Enter English score: "))
        math = float(input("Enter Math score: "))

        student = Student(name, korean, english, math)
        students.append(student)

    print("\nAverage scores:")
    for student in students:
        average_score = student.calculate_average()
        print(f"{student.name}: {average_score:.2f}")


if __name__ == "__main__":
    main()




