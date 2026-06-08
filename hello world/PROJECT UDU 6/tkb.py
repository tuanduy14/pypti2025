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