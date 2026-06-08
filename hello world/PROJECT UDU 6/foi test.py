import pygame
import csv

# Constants
FILE_NAME = 'qlsv.csv'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Student Management System")
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 28)

# Student class
class Student:
    def __init__(self, ID, Name, Class, age):
        self.Class = Class
        self.Name = Name
        self.ID = ID
        self.age = age

# Read students from CSV
def read_student_to_csv():
    students = []
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row:
                    Name, ID, age, Class = row[0], row[1], row[2], row[3]
                    student = Student(ID, Name, Class, age)
                    students.append(student)
    except FileNotFoundError:
        pass
    return students

# Write students to CSV (with safe handling)
def write_student_to_csv(students):
    try:
        with open(FILE_NAME, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID", "Age", "Class"])
            for student in students:
                writer.writerow([student.Name, student.ID, student.age, student.Class])
    except PermissionError:
        print("Permission denied. Make sure the file is not open in another program and try again.")

# Display Text on the screen
def display_text(text, x, y, color=BLACK, font_type=font):
    label = font_type.render(text, True, color)
    screen.blit(label, (x, y))

# Draw button
def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    display_text(text, x + 10, y + 10, text_color)

# Show all students
def show_all_students(students):
    y_offset = 100
    for student in students:
        display_text(f"Name: {student.Name}, ID: {student.ID}, Age: {student.age}, Class: {student.Class}",
                     50, y_offset)
        y_offset += 40
        if y_offset > 500:
            break  # Prevent overflow

# Add new student through Pygame input
def add_student(students):
    name_input = ""
    id_input = ""
    age_input = ""
    class_input = ""
    input_mode = 0
    input_complete = False

    while not input_complete:
        screen.fill(WHITE)
        display_text("Enter Student Information", 50, 50, BLUE)

        draw_button("Submit", 550, 450, 200, 50, GREEN, WHITE)
        draw_button("Cancel", 550, 520, 200, 50, RED, WHITE)

        # Display inputs
        display_text("Name: " + name_input, 50, 150)
        display_text("ID: " + id_input, 50, 200)
        display_text("Age: " + age_input, 50, 250)
        display_text("Class: " + class_input, 50, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return students

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 550 <= x <= 750 and 450 <= y <= 500:
                    # Validate the inputs before submitting
                    if id_input.isdigit() and age_input.isdigit():
                        new_student = Student(id_input, name_input, class_input, age_input)
                        students.append(new_student)
                        write_student_to_csv(students)
                        input_complete = True
                    else:
                        display_text("Please enter valid ID and Age!", 50, 350, RED)
                elif 550 <= x <= 750 and 520 <= y <= 570:
                    # Cancel button
                    input_complete = True

            if event.type == pygame.KEYDOWN:
                if input_mode == 0:
                    if event.key == pygame.K_RETURN:
                        input_mode = 1
                    elif event.key == pygame.K_BACKSPACE:
                        name_input = name_input[:-1]
                    else:
                        name_input += event.unicode
                elif input_mode == 1:
                    if event.key == pygame.K_RETURN:
                        input_mode = 2
                    elif event.key == pygame.K_BACKSPACE:
                        id_input = id_input[:-1]
                    else:
                        id_input += event.unicode
                elif input_mode == 2:
                    if event.key == pygame.K_RETURN:
                        input_mode = 3
                    elif event.key == pygame.K_BACKSPACE:
                        age_input = age_input[:-1]
                    else:
                        age_input += event.unicode
                elif input_mode == 3:
                    if event.key == pygame.K_RETURN:
                        input_mode = 4
                    elif event.key == pygame.K_BACKSPACE:
                        class_input = class_input[:-1]
                    else:
                        class_input += event.unicode

        pygame.display.update()

    return students

# Delete student from list
def delete_student(students):
    screen.fill(WHITE)
    display_text("Select a student to delete:", 50, 50, BLUE)

    # Show all students to select
    y_offset = 100
    for i, student in enumerate(students):
        display_text(f"{i + 1}. {student.Name}", 50, y_offset)
        y_offset += 40

    draw_button("Delete", 550, 450, 200, 50, RED, WHITE)
    draw_button("Cancel", 550, 520, 200, 50, GREEN, WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return students

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 550 <= x <= 750 and 450 <= y <= 500:
                # Delete selected student
                selection = (y - 100) // 40
                if 0 <= selection < len(students):
                    del students[selection]
                    write_student_to_csv(students)
                    return students  # Update the list after deletion
            elif 550 <= x <= 750 and 520 <= y <= 570:
                return students  # Cancel button

        pygame.display.update()

    return students

# Main game loop
def main():
    students = read_student_to_csv()

    # Main loop
    running = True
    while running:
        screen.fill(WHITE)

        # Display Menu
        display_text("Student Management System", 250, 50, BLUE)

        # Display the buttons
        draw_button("Add Student", 50, 150, 200, 50, GREEN, WHITE)
        draw_button("Delete Student", 50, 220, 200, 50, GREEN, WHITE)
        draw_button("Show Students", 50, 290, 200, 50, GREEN, WHITE)
        draw_button("Save & Exit", 50, 360, 200, 50, RED, WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Add Student Button
                if 50 <= x <= 250 and 150 <= y <= 200:
                    students = add_student(students)

                # Delete Student Button
                if 50 <= x <= 250 and 220 <= y <= 270:
                    students = delete_student(students)

                # Show Students Button
                if 50 <= x <= 250 and 290 <= y <= 340:
                    screen.fill(WHITE)
                    show_all_students(students)
                    pygame.display.update()

                # Save & Exit Button
                if 50 <= x <= 250 and 360 <= y <= 410:
                    write_student_to_csv(students)
                    print("Data saved!")
                    running = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
