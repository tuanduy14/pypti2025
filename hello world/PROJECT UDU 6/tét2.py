class Schedule:
    def __init__(self, Day, Start, End, Course):
        self.Day = Day
        self.Start = Start
        self.End = End
        self.Course = Course


# Hàm hiển thị các menu
def opt_4_teach():
    print("\n------| Creative to Schedule |-------")
    print("| Option 1: Create new schedule.  |")
    print("| Option 2: Show schedules.       |")
    print("| Option 3: Update schedules.     |")
    print("| Option 4: Save & Exit.          |")
    print("-----------------------------------")
    return select_in_range("Select an option (1 - 4): ", 1, 4)  # Nhận lựa chọn của người dùng


# Hàm in danh sách lịch học theo bảng
def print_schedules_table(schedules):
    if not schedules:
        print("\nNo schedules available.")
        return
    print("\nSchedule List:")
    print("{:<5} {:<10} {:<15} {:<15} {:<20}".format("No.", "Day", "Start Time", "End Time", "Course"))
    for idx, sched in enumerate(schedules, 1):
        print("{:<5} {:<10} {:<15} {:<15} {:<20}".format(idx, sched.Day, sched.Start, sched.End, sched.Course))


# Hàm cập nhật lịch học
def update_schedules(schedules):
    if not schedules:
        print("No schedules to update!!!")
        return schedules

    print_schedules_table(schedules)

    # Chọn lịch để cập nhật
    index = select_in_range(f"Enter a schedule number (1 - {len(schedules)}): ", 1, len(schedules)) - 1

    print("\n------| Update Student Schedule |-----")
    print("| 1. Update Day               |")
    print("| 2. Update Start Time        |")
    print("| 3. Update End Time          |")
    print("| 4. Update Course            |")
    print("------------------------------------")

    choice = select_in_range("Select an option (1 - 4): ", 1, 4)

    # Xử lý cập nhật theo lựa chọn của người dùng
    if choice == 1:
        schedules[index].Day = input("Enter new day (e.g., Monday): ")
    elif choice == 2:
        schedules[index].Start = input("Enter new start time (e.g., 09:00 AM): ")
    elif choice == 3:
        schedules[index].End = input("Enter new end time (e.g., 10:00 AM): ")
    elif choice == 4:
        schedules[index].Course = input("Enter new course name: ")

    return schedules


# Hàm kiểm tra và nhập liệu từ người dùng trong khoảng cho phép
def select_in_range(prompt, min_value, max_value):
    while True:
        try:
            choice = int(input(prompt))
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")