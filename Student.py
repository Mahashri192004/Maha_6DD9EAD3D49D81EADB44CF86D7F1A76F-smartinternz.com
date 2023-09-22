class Student:

  def __init__(self, name,roll_number, cgpa):
    self.name = name 
    self.roll_number = roll_number 
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descendingorder of CGPA
  sorted_students = sorted(student_list, 
                     key=lambda student: student.cgpa,
                     reverse=True)
  return sorted_students


# Example usage:
students = [
   Student("shri", "R018", 9.8),
   Student("Nandhu", "R019", 8.9),
   Student("mahi", "R020", 9.7),
   Student("muhi", "R021", 8.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students 
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))