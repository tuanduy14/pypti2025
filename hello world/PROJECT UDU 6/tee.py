import csv
import random
from calendar import calendar

from tabulate import tabulate
from datetime import datetime

FILE_NAME_1 = 'qlsv_teacher.csv'
FILE_NAME_2 = "qlsv_student.csv"
FILE_NAME_3 = 'schedule.csv'
FILE_NAME_4 = "calendar.csv"
FILE_NAME_5 = "student_scores.csv"

class Student:
    def __init__(self, ID, Name, Class, sex, ):
        self.Class = Class
        self.Name = Name
        self.ID = ID
        self.sex = sex


class School_Schedule:
    def __init__(self, Day, Start, End, Course):
        self.Day = Day
        self.Start = Start
        self.End = End
        self.Course = Course

    def __repr__(self):
        return f"School_Schedule(Day={self.Day}, Start={self.Start}, End={self.End}, Course={self.Course})"

    def to_list(self):
        return [self.Day, self.Start, self.End, self.Course]

def read_schedule():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    schedule = []

    print("\n------| Select Days for Schedule |------")
    for idx, day in enumerate(days_of_week, 1):
        print(f"{idx}. {day}")

    selected_days = []
    while True:
        try:
            days_input = input("Enter the numbers corresponding to the days: ")
            day_numbers = list(map(int, days_input.split()))

            if all(1 <= num <= 7 for num in day_numbers):
                selected_days = [days_of_week[num - 1] for num in day_numbers]
                break
            else:
                print("Invalid input. Please select numbers between 1 and 7 with space.")
        except ValueError:
            print("Invalid input. Please select numbers between 1 and 7 with space.")

    for day in selected_days:
        print('-----')
        Start = input(f"Enter Start Time for {day}: ")
        End = input(f"Enter End Time for {day}: ")
        Course = input(f"Enter Course Name for {day}: ")
        schedule.append(School_Schedule(day, Start, End, Course))

    return schedule

def add_another_schedule():
    while True:
        another = input("\nDo you want to add another schedule? (y/n): ").strip().lower()
        if another == 'y':
            return True
        elif another == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def read_schedules():
    schedules = []
    while True:
        print("------")
        schedule = read_schedule()
        schedules.extend(schedule)

        if not add_another_schedule():
            break

    return schedules

def print_schedules_table(schedules):
    table = []
    for i, schedule in enumerate(schedules, start=1):
        table.append([i, schedule.Day, schedule.Start, schedule.End, schedule.Course])

    headers = ["#", "Day", "Start Time", "End Time", "Course"]
    print("=== School Schedule ===")
    print(tabulate(table, headers, tablefmt="grid"))

def write_schedules_to_csv(schedules):
    with open(FILE_NAME_3, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Start", "End", "Course"])
        for schedule in schedules:
            writer.writerow(schedule.to_list())

def read_schedules_to_csv():
    schedules = []
    try:
        with open(FILE_NAME_3, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 4:
                    schedules.append(School_Schedule(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        print(f"The file {FILE_NAME_3} does not exist. Starting with an empty schedule.")

    return schedules


# Nhập từng học sinh
def read_student():
    Name = input("Enter name: ")
    ID = input("Enter ID: ")
    sex = input("Enter sex (M/F): ")
    Class = input("Enter class: ")
    student = Student(ID, Name, Class, sex)

    return student


# In từng học sinh
def print_student(student):
    print("Student Name: ", student.Name)
    print("Student ID: ", student.ID)
    print("Student sex: ", student.sex)
    print("Student Class: ", student.Class)


# Nhập nhiều học sinh
def read_students():
    students = []
    total_student = int(input("How many students: "))
    for i in range(total_student):
        print("Student " + str(i + 1))
        stu = read_student()
        students.append(stu)
    return students


# In nhiều học sinh
def print_students(students):
    for i in range(len(students)):
        print("------")
        print("Student " + str(i + 1) + ":")
        print_student(students[i])


# Ghi vào file cvs
def write_student_to_csv(students):
    with open(FILE_NAME_1, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "ID", "sex", "Class"])
        for student in students:
            writer.writerow([student.Name, student.ID, student.sex, student.Class])


# Đọc trong file cvs
def read_student_to_csv():
    students = []
    with open(FILE_NAME_1, mode="r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                Name, ID, sex, Class = row[0], row[1], row[2], row[3]
                student = Student(ID, Name, Class, sex)
                students.append(student)
    return students


# Vẽ menu
def show_menu_manager():
    print("           | MAIN MENU |           ")
    print("-----------------------------------")
    print("| Option 1: For Teachers          |")
    print("| Option 2: For Students          |")
    print("| Option 3: Exit                  |")
    print("-----------------------------------")


# Vẽ menu teacher
def show_menu_teachers():
    print("----------|FOR TEACHERS|-----------")
    print("| Option 1: Excel students.       |")
    print("| Option 2: Random ID.            |")
    print("| Option 3: Student attendance    |")
    print("| Option 4: Excel schedules.      |")
    print("| Option 5: Score management      |")
    print("| Option 6: Exit                  |")
    print('-----------------------------------')



def opt_1_teach():
    print("------|Creative to students|-------")
    print("| Option 1: Creative to students. |")
    print("| Option 2: Show students.        |")
    print("| Option 3: Add student.          |")
    print("| Option 4: Update student.       |")
    print("| Option 5: Delete student.       |")
    print("| Option 6: Save to Exit.         |")
    print("-----------------------------------")


def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)

    choice = int(choice)
    return choice


def add_student(students):
    print("-----|Enter Add Your Students|-----")
    total_students = int(input("How many students do you want to add: "))
    for i in range(total_students):
        print(f"Student {i + 1}:")
        new_student_Name = input("Enter name: ")
        new_student_ID = input("Enter ID: ")
        new_student_age = input("Enter sex: ")
        new_student_Class = input("Enter class: ")
        new_student = Student(new_student_Name, new_student_ID, new_student_age, new_student_Class)
        students.append(new_student)
    print(f"Added {total_students} students successfully!")
    return students


def update_student(students):
    print_students(students)
    find = select_in_range("Enter a update student (1 - " + str(len(students)) + "): ", 1, int(len(students)))

    print("------|Update Student?|-----")
    print("| 1. Name                  |")
    print("| 2. ID                    |")
    print("| 3. sex                   |")
    print("| 4. Class                 |")
    print("----------------------------")

    choice = select_in_range("Select a number (1 - 4): ", 1, 4)
    if choice == 1:
        students[find - 1].Name = input("Enter new name: ")
    elif choice == 2:
        students[find - 1].ID = input("Enter new ID: ")
    elif choice == 3:
        students[find - 1].sex = input("Enter new sex: ")
    elif choice == 4:
        students[find - 1].Class = input("Enter new class: ")

    print("Update Successfully!!!")
    return students


def delete_student(students):
    print_students(students)
    choice = select_in_range("Enter a delete student (1 - " + str(len(students)) + "): ", 1, int(len(students)))
    new_list_student = []
    for i in range(len(students)):
        if i == choice - 1:
            continue

        new_list_student.append(students[i])

    students = new_list_student
    print("Remove Successfully!!!")

    return students


def opt_2_teach(students):
    if not students:
        print("NO STUDENT")
        return None

    students_random = random.choice(students)
    stu_return = str(students_random.Name) + " - " + str(students_random.ID)
    return stu_return


def opt_3_teach(students):
    if not students:
        print("NO STUDENT")
        return None

    today = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME_1, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    if today is not data[0]:
        data[0].append(today)

    day = data[0].index(today)

    present = 0
    absent = 0

    for student in students:
        for row in data[1:]:
            if row[1] == student.ID:
                student_row = row
                break

        while len(student_row) < len(data[0]):
            student_row.append("v")

            print("Student: " + student.Name)
            status = select_in_range("Attendance [0 (vkp)/1 (*)/2 (v)]: ", 0, 2)
            if status == 1:
                student_row[day] = "*"
                present += 1
            elif status == 2:
                student_row[day] = "v"
                absent += 1
            elif status == 0:
                student_row[day] = "vkp"
                absent += 1

    with open(FILE_NAME_1, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("--------")
    print("Students present : (" + str(present) + "/" + str(present + absent) + ")")


def opt_4_teach():
    print("------|Creative to schedule|-------")
    print("| Option 1: Creative to schedules.|")
    print("| Option 2: Show schedule.        |")
    print("| Option 3: Update schedules.     |")
    print("| Option 4: Save to Exit.         |")
    print("-----------------------------------")


def update_schedules(schedules):
    print_schedules_table(schedules)
    if not schedules:
        print("No schedules to update!!!")
        return schedules

    index = select_in_range("Enter a update schedule (1 - " + str(len(schedules)) + "): ", 1, int(len(schedules))) - 1

    print("------|Update Student?|-----")
    print("| 1. Update Day            |")
    print("| 2. Update Start Time     |")
    print("| 3. Update End Time       |")
    print("| 4. Update Course         |")
    print("----------------------------")

    choice = select_in_range("Select an option (1 - 4): ", 1, 4)
    if choice == 1:
        schedules[index].Day = input("Enter new day: ")
    elif choice == 2:
        schedules[index].Start = input("Enter new start time: ")
    elif choice == 3:
        schedules[index].End = input("Enter new end time: ")
    elif choice == 4:
        schedules[index].Course = input("Enter new course: ")

    return schedules


def show_menu_students():
    print("----------|FOR STUDENTS|-----------")
    print("| Option 1: Calenders             |")
    print("| Option 2: Points                |")
    print("| Option 3: Exit.                 |")
    print("-----------------------------------")

def show_menu_calenders():
    print("----------|FOR STUDENTS|-----------")
    print("| Option 1: Select Calenders      |")
    print("| Option 2: Show Calenders        |")
    print("| Option 3: Exit.                 |")
    print("-----------------------------------")


def print_calenders_table(calendars):
    if not calendars:
        print("No calendars available.")
        return

    print(f"{'Course':<20}{'Day':<15}{'Time':<15}{'Room':<15}")
    print("-" * 65)

    for schedule in calendars:
        print(f"{schedule.Course:<20}{schedule.Day:<15}{schedule.Time:<15}{schedule.Room:<15}")


def show_calenders_for_student(student_id):
    calendars = read_calendar_for_student(student_id)
    print_calenders_table(calendars)


def read_calendar_from_schedule():
    calendars = []
    try:
        with open(FILE_NAME_3, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Bỏ qua dòng tiêu đề
            for row in reader:
                if len(row) == 4:
                    calendars.append(School_Schedule(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        print(f"{FILE_NAME_3} not found. Make sure the schedule file exists.")
    return calendars


def print_calendar(calendar):
    print("Day :", calendar.Day)
    print("Start: ", calendar.Start)
    print("End: ", calendar.End)
    print("Subject: ", calendar.Subject)

def input_calendar():
    calendars = []
    all_calendars = 7
    for i in range(all_calendars):
        print("------")
        print("Calendar " + str(i + 1))
        day = input("Enter Day: ")
        start = input("Enter Start Time: ")
        end = input("Enter End Time: ")
        subject = input("Enter Subject: ")
        calendar = School_Schedule(day, start, end, subject)
        calendars.append(calendar)
    return calendars

def in_calendar_to_table(calendars):
    table = []
    for i, calendar in enumerate(calendars, start=1):
        table.append([i, calendar.Day, calendar.Start, calendar.End, calendar.Subject])
    headers = ["#", "Day", "Start Time", "End Time", "Subject"]
    print("======= Student Calendars ======")
    print(tabulate(table, headers, tablefmt="grid"))


def write_calendar_to_csv(calendars):
    with open(FILE_NAME_4, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Start", "End", "Subject"])
        for calendar in calendars:
            writer.writerow([calendar.Day, calendar.Start, calendar.End, calendar.Subject])
    print("Calendar saved successfully!")

def read_calendar_to_csv():
    calendars = []
    try:
        with open(FILE_NAME_4, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 4:
                    calendars.append(School_Schedule(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        print(f"{FILE_NAME_4} not found, starting with an empty calendar.")
    return calendars


def read_calendar_for_student(student_id):
    calendars = []
    try:
        with open(FILE_NAME_3, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 5 and row[4] == student_id:
                    calendars.append(School_Schedule(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
         print(f"{FILE_NAME_3} not found. Make sure the schedule file exists.")
    return calendars
def select_schedules_for_student():
    try:
        schedules = read_schedules_to_csv()
        if not schedules:
            print("No schedules available.")
            return []

        print("\n=== Available Schedules ===")
        print_schedules_table(schedules)

        selected_schedules = []
        while len(selected_schedules) < 3:
            print(f"\nYou need to select at least {3 - len(selected_schedules)} more schedules.")
            try:
                choice = select_in_range(
                    "Select a schedule by number (1 - {}): ".format(len(schedules)), 1, len(schedules)
                )
                selected_schedule = schedules[choice - 1]
                if selected_schedule not in selected_schedules:
                    selected_schedules.append(selected_schedule)
                    print(f"Added schedule: {selected_schedule.Course} on {selected_schedule.Day}")
                else:
                    print("You already selected this schedule.")
            except Exception as e:
                print(f"Invalid input: {e}")

        print("\n=== Your Selected Schedules ===")
        print_schedules_table(selected_schedules)

        # Lưu danh sách thời khóa biểu đã chọn vào file CSV
        save_schedules_to_csv(selected_schedules)

        # Hiển thị lại thời khóa biểu từ đối tượng đã chọn
        print("\n=== Final Selected Schedules ===")
        print_schedules_table(selected_schedules)

        return selected_schedules
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def save_schedules_to_csv(selected_schedules, filename="selected_schedules.csv"):
    """
    Lưu danh sách thời khóa biểu đã chọn vào file CSV.

    :param selected_schedules: Danh sách các thời khóa biểu đã chọn.
    :param filename: Tên file CSV sẽ lưu.
    """
    try:
        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            # Ghi tiêu đề cột
            writer.writerow(["Day", "Start", "End", "Course"])

            # Ghi từng dòng dữ liệu
            for schedule in selected_schedules:
                writer.writerow([schedule.Day, schedule.Start, schedule.End, schedule.Course])

        print(f"Schedules saved to {filename} successfully!")
    except Exception as e:
        print(f"Failed to save schedules: {e}")



def show_selected_schedules_from_csv(filename="selected_schedules.csv"):
    """
    Hiển thị thời khóa biểu từ file CSV.

    :param filename: Tên file CSV chứa thời khóa biểu.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Đọc tiêu đề
            header = next(reader, None)
            if header:
                print("\n=== Selected Schedules ===")
                print("{:<10} {:<15} {:<15} {:<10}".format(*header))
                print("-" * 55)

            # Đọc từng dòng dữ liệu
            for row in reader:
                print("{:<10} {:<15} {:<15} {:<10}".format(*row))
    except Exception as e:
        print(f"Failed to read schedules from {filename}: {e}")




def who_are_you():
    try:
        with open(FILE_NAME_1, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            student_id = input("Enter id: ").strip()

            for row in reader:
                if len(row) > 1 and row[1] == student_id:
                    print(f"Hello {row[0]} (ID: {row[1]}), class {row[3]}.")
                    return True

            print("You are not in class.")
            return False
    except FileNotFoundError:
        print(f"File {FILE_NAME_1} không tồn tại.")
        return False
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")
        return False



class StudentScore:
    def __init__(self, student_id, name, subject, score):
        self.student_id = student_id
        self.name = name
        self.subject = subject
        self.score = score

def show_score_menu():
    print("----------| SCORE MANAGEMENT |-----------")
    print("| Option 1: Add Scores                   |")
    print("| Option 2: View Scores                  |")
    print("| Option 3: Edit Scores                  |")
    print("| Option 4: Delete Scores                |")
    print("| Option 5: Calculate GPA                |")
    print("| Option 6: Exit                         |")
    print("-----------------------------------------")


def add_scores(scores):
    total_students = int(input("Enter the number of students to add scores for: "))
    for _ in range(total_students):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        subject = input("Enter Subject: ")
        score = float(input("Enter Score: "))
        scores.append(StudentScore(student_id, name, subject, score))
    print(f"{total_students} scores added successfully!")

def view_scores(scores):
    if not scores:
        print("No scores available to display!")
        return

    print("\nFilter options:")
    print("1. View all scores")
    print("2. Search by Student ID")
    print("3. Search by Student Name")
    print("4. Search by Subject")
    choice = int(input("Select an option: "))

    if choice == 1:
        table = [[s.student_id, s.name, s.subject, s.score] for s in scores]
        headers = ["Student ID", "Name", "Subject", "Score"]
        print(tabulate(table, headers, tablefmt="grid"))
        input('\nPress Enter to continue.\n')
    elif choice == 2:
        student_id = input("Enter Student ID: ")
        filtered_scores = [s for s in scores if s.student_id == student_id]
        if filtered_scores:
            table = [[s.student_id, s.name, s.subject, s.score] for s in filtered_scores]
            headers = ["Student ID", "Name", "Subject", "Score"]
            print(tabulate(table, headers, tablefmt="grid"))
            input('\nPress Enter to continue.\n')
        else:
            print("No scores found for the given Student ID.")
            input('\nPress Enter to continue.\n')
    elif choice == 3:
        name = input("Enter Student Name: ")
        filtered_scores = [s for s in scores if s.name.lower() == name.lower()]
        if filtered_scores:
            table = [[s.student_id, s.name, s.subject, s.score] for s in filtered_scores]
            headers = ["Student ID", "Name", "Subject", "Score"]
            print(tabulate(table, headers, tablefmt="grid"))
            input('\nPress Enter to continue.\n')
        else:
            print("No scores found for the given Student Name.")
            input('\nPress Enter to continue.\n')
    elif choice == 4:
        subject = input("Enter Subject: ")
        filtered_scores = [s for s in scores if s.subject.lower() == subject.lower()]
        if filtered_scores:
            table = [[s.student_id, s.name, s.subject, s.score] for s in filtered_scores]
            headers = ["Student ID", "Name", "Subject", "Score"]
            print(tabulate(table, headers, tablefmt="grid"))
            input('\nPress Enter to continue.\n')
        else:
            print("No scores found for the given Subject.")
            input('\nPress Enter to continue.\n')
    else:
        print("Invalid option!")
        input('\nPress Enter to continue.\n')

def edit_scores(scores):
    if not scores:
        print("No scores available to edit!")
        return

    student_id = input("Enter Student ID to edit: ")
    subject = input("Enter Subject to edit: ")

    for score in scores:
        if score.student_id == student_id and score.subject.lower() == subject.lower():
            print(f"Current score for {score.name} in {score.subject}: {score.score}")
            new_score = float(input("Enter the new score: "))
            score.score = new_score
            print("Score updated successfully!")
            return

    print("No matching record found to edit!")

def delete_scores(scores):
    if not scores:
        print("No scores available to delete!")
        return

    print("\nDelete options:")
    print("1. Delete by Student ID")
    print("2. Delete by Subject")
    print("3. Delete All Scores")
    choice = int(input("Select an option: "))

    if choice == 1:
        student_id = input("Enter Student ID to delete: ")
        scores[:] = [s for s in scores if s.student_id != student_id]
        print(f"Scores for Student ID {student_id} deleted successfully!")
    elif choice == 2:
        subject = input("Enter Subject to delete: ")
        scores[:] = [s for s in scores if s.subject.lower() != subject.lower()]
        print(f"Scores for Subject {subject} deleted successfully!")
    elif choice == 3:
        scores.clear()
        print("All scores deleted successfully!")
    else:
        print("Invalid option!")

def save_scores_to_file(scores):
    with open(FILE_NAME_5, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Name", "Subject", "Score"])
        for score in scores:
            writer.writerow([score.student_id, score.name, score.subject, score.score])
    print(f"Scores saved successfully to {FILE_NAME_5}!")

def load_scores_from_file():
    scores = []
    try:
        with open(FILE_NAME_5, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) == 4:
                    scores.append(StudentScore(row[0], row[1], row[2], float(row[3])))
        print(f"Scores loaded successfully from {FILE_NAME_5}!")
    except FileNotFoundError:
        print(f"No saved scores found in {FILE_NAME_5}.")
    return scores

def calculate_gpa(scores):
    if not scores:
        print("No scores available to calculate GPA!")
        return

    student_scores = {}
    for score in scores:
        if score.student_id not in student_scores:
            student_scores[score.student_id] = {"name": score.name, "total_score": 0, "count": 0}
        student_scores[score.student_id]["total_score"] += score.score
        student_scores[score.student_id]["count"] += 1

    print("\nGPA of each student:")
    table = []
    headers = ["Student ID", "Name", "GPA"]
    for student_id, data in student_scores.items():
        gpa = data["total_score"] / data["count"]
        table.append([student_id, data["name"], round(gpa, 2)])
    print(tabulate(table, headers, tablefmt="grid"))


def view_score_for_stu(scores):
    if not scores:
        print("No scores available to display!")
        return

    student_id = input("Enter Student ID: ")
    filtered_scores = [s for s in scores if s.student_id == student_id]
    if filtered_scores:
        table = [[s.student_id, s.name, s.subject, s.score] for s in filtered_scores]
        headers = ["Student ID", "Name", "Subject", "Score"]
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print("No scores found for the given Student ID.")

def main():
    while True:
        show_menu_manager()
        choice_manager = select_in_range("Select an option (1 - 3): ", 1, 3)

        if choice_manager == 1:
            while True:
                show_menu_teachers()
                choice_teach = select_in_range("Select an option (1 - 6): ", 1, 6)

                if choice_teach == 1:

                    try:
                        students = read_student_to_csv()
                        print("Loadinggg...........")
                    except:
                        print("Welcome, first user!!")

                    while True:
                        opt_1_teach()
                        choice_ex_stu = select_in_range("Select an option (1 - 6): ", 1, 6)

                        if choice_ex_stu == 1:
                            students = read_students()

                        try:
                            if choice_ex_stu == 2:
                                print_students(students)
                                input("\nPress Enter to continue.\n")
                            elif choice_ex_stu == 3:
                                students = add_student(students)
                                input("\nPress Enter to continue.\n")
                            elif choice_ex_stu == 4:
                                students = update_student(students)
                                input("\nPress Enter to continue.\n")
                            elif choice_ex_stu == 5:
                                students = delete_student(students)
                                input("\nPress Enter to continue.\n")
                            elif choice_ex_stu == 6:
                                write_student_to_csv(students)
                                print("Save Data Successfully !!!! ")
                                break

                        except:
                            print("You don't have any students yet!!! ")
                            input("\nPress Enter to continue.\n")

                try:
                    students = read_student_to_csv()
                    if choice_teach == 2:

                        choice_students = opt_2_teach(students)

                        if choice_students:
                            print("Randomly selected:", choice_students)
                            input("\nPress Enter to continue.\n")

                    elif choice_teach == 3:
                        opt_3_teach(students)
                        input("\nPress Enter to continue.\n")

                    elif choice_teach == 4:
                        try:
                            schedules = read_schedules_to_csv()
                            print("Loadinggg...........")
                        except:
                            print("Welcome, first user!!")

                        while True:
                            opt_4_teach()
                            choice_ex_sche = select_in_range("Select an option (1 - 4): ", 1, 4)

                            if choice_ex_sche == 1:
                                schedules = read_schedules()
                            try:
                                if choice_ex_sche == 2:
                                    print_schedules_table(schedules)
                                    input("\nPress Enter to continue.\n")
                                elif choice_ex_sche == 3:
                                    schedules = update_schedules(schedules)
                                    input("\nPress Enter to continue.\n")
                                elif choice_ex_sche == 4:
                                    write_schedules_to_csv(schedules)
                                    print("Save Data Successfully !!!! ")
                                    input("\nPress Enter to continue.\n")
                                    break

                            except:
                                print("You don't have any schedules yet!!! ")
                                input("\nPress Enter to continue.\n")

                    elif choice_teach == 5:
                        scores=load_scores_from_file()
                        while True:
                            show_score_menu()
                            choice = input("Select an option (1-6): ")
                            if choice == "1":
                                add_scores(scores)
                            elif choice == "2":
                                view_scores(scores)
                            elif choice == "3":
                                edit_scores(scores)
                            elif choice == "4":
                                delete_scores(scores)
                            elif choice == "5":
                                calculate_gpa(scores)
                            elif choice == "6":
                                save_scores_to_file(scores)
                                scores=load_scores_from_file()
                                print("Exiting Score Management...")
                                break
                            else:
                                print("Invalid option! Please select again.")


                    elif choice_teach == 6:
                        print("Exit Successfully !!!! ")
                        break
                except:
                    print("You don't have any students yet!!! ")
                    input("\nPress Enter to continue.\n")


        elif choice_manager == 2:

            if not who_are_you():
                continue

            while True:

                show_menu_students()

                choice_stu = select_in_range("Select an option (1 - 3): ", 1, 3)

                if choice_stu == 3:
                    print("Exit Successfully !!!! ")

                    break


                if choice_stu ==2:
                    view_score_for_stu(scores)
                    input('\nPress Enter to continue.\n')
                    break

                calendars = []

                try:

                    calendars = read_calendar_to_csv()

                    print("Loadinggg...........")

                except:

                    print("Welcome, first user!!")

                while True:

                    show_menu_calenders()

                    choice_ex_sche = select_in_range("Select an option (1 - 3): ", 1, 3)

                    if choice_ex_sche == 1:
                        select_schedules_for_student()

                    try:

                        if choice_ex_sche == 2:

                            show_selected_schedules_from_csv()

                        elif choice_ex_sche == 3:

                            write_calendar_to_csv(calendars)

                            input("\nPress Enter to continue.\n")

                            break

                    except:

                        print("You don't have any calendar yet!!! ")

                        input("\nPress Enter to continue.\n")



        elif choice_manager == 3:
            print("Exit Successfully !!!! ")
            break


main()