class Student:
	def __init__(self, student_id, name, age, course):
		self.student_id = student_id
		self.name = name
		self.age = age
		self.course = course

	def display_details(self):
		print(f"Student ID: {self.student_id}")
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		print(f"Course: {self.course}")


student = Student(101, "Amruta", 21, "Computer Engineering")
student.display_details()
