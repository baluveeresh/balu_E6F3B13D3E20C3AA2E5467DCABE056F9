def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)
 
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("Ajith", "A001", 3.8),
    Student("Balu", "A002", 3.5),
    Student("Dinesh", "A003", 3.9),
    Student("Ikesh", "A004", 3.7)
]

# Sort the list of students based on CGPA
sort_students(students)

# Print the sorted list
for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")