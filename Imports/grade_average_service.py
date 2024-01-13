
def calculate_homework(homework_assiggments_arg):
    sum_of_grades = 0
    for homework in homework_assiggments_arg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(homework_assiggments_arg))
    print(final_grade)