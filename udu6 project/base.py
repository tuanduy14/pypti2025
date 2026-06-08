import csv
import random

FILE_NAME = 'qlsv.csv'

class Student:
	def __init__(self, ID, Name, Class, age):
		self.Class = Class
		self.Name = Name
		self.ID = ID
		self.age = age

def read_student():
	Name = input("Enter name: ")
	ID = input("Enter ID: ")
	age = input("Enter age: ")
	Class = input("Enter class: ")
	student = Student(ID, Name, Class, age)

	return student

def print_student(student):
	print( "Student Name: ", student.Name)
	print( "Student ID: ", student.ID)
	print( "Student Age: ", student.age)
	print( "Student Class: ", student.Class)

def read_students():
	students = []
	total_student = int(input("How many students: "))
	for i in range(total_student):
		print("Student " + str(i + 1))
		stu = read_student()
		students.append(stu)
	return students

def print_students(students):
	for i in range(len(students)):
		print("-----")
		print("Student " + str(i + 1) + ":")
		print_student(students[i])

def write_student_to_csv(students):
	with open(FILE_NAME, mode="w", newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Name", "ID" , "Age", "Class"])
		for student in students:
			writer.writerow([student.Name, student.ID, student.age, student.Class])

def read_student_to_csv():
	students = []
	with open(FILE_NAME, mode="r") as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			if row:
				Name, ID, age, Class = row[0], row[1], row[2], row[3]
				student = Student(ID, Name, Class, age)
				students.append(student)
	return students

def show_menu():
	print("           | MAIN MENU |           ")
	print("-----------------------------------")
	print("| Option 1: Creative to students. |")
	print("| Option 2: Show students.        |")
	print("| Option 3: Random ID.            |")
	print("| Option 4: Add student.          |")
	print("| Option 5: Update student.       |")
	print("| Option 6: Delete student.       |")
	print("| Option 7: Save to Exit.         |")
	print("-----------------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice

def random_ID(students):
	if not students:
		print("NO STUDENT")
		return None

	students_random = random.choice(students)
	return students_random.ID

def add_student(students):
    print("-----|Enter Add Your Students|-----")
    total_students = int(input("How many students do you want to add: "))
    for i in range(total_students):
        print(f"Student {i + 1}:")
        new_student_Name = input("Enter name: ")
        new_student_ID = input("Enter ID: ")
        new_student_age = input("Enter age: ")
        new_student_Class = input("Enter class: ")
        new_student = Student(new_student_Name, new_student_ID, new_student_age, new_student_Class)
        students.append(new_student)
    print(f"Added {total_students} students successfully!")
    return students

def update_student(students):
	print_students(students)
	find = select_in_range("Enter to update student (1 - " + str(len(students)) + "): ", 1, int(len(students)))

	print("-----|Update Student?|-----")
	print("| 1. Name                  |")
	print("| 2. ID                    |")
	print("| 3. Age                   |")
	print("| 4. Class                 |")
	print("----------------------------")

	choice = select_in_range("Select a number (1 - 4): ", 1, 4)
	if choice == 1:
		students[find - 1].Name = input("Enter new name: ")
	elif choice == 2:
		students[find - 1].ID = input("Enter new ID: ")
	elif choice == 3:
		students[find - 1].age = input("Enter new age: ")
	elif choice == 4:
		students[find - 1].Class = input("Enter new class: ")

	print("Update Successfully!!!")
	return students


def delete_student(students):
	print_students(students)
	choice = select_in_range("Enter a delete student (1 - " + str(len(students)) + "): ", 1, int(len(students)))
	students.pop(choice - 1)
	print("Remove Successfully!!!")
	return students

def main():

	try:
		students = read_student_to_csv()
		print("Loadinggg...........")
	except:
		print("Welcome, first user!!")

	while True:
		show_menu()
		choice = select_in_range("Select an option (1 - 7): ", 1, 7)
		if choice == 1:
			students = read_students()
			input("\nPress Enter to continue.\n")
		elif choice == 2:
			print_students(students)
			input("\nPress Enter to continue.\n")
		elif choice == 3:
			ID_students = random_ID(students)
			if ID_students:
				print("Randomly selected ID: ", ID_students)
			input("\nPress Enter to continue.\n")
		elif choice == 4:
			students = add_student(students)
			input("\nPress Enter to continue.\n")
		elif choice == 5:
			students = update_student(students)
			input("\nPress Enter to continue.\n")
		elif choice == 6:
			students = delete_student(students)
			input("\nPress Enter to continue.\n")
		elif choice == 7:
			write_student_to_csv(students)
			print("Save Data Successfully !!!! ")
			break

main()