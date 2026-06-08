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