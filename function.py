def make_student(name, scores):
    average = sum(scores) / len(scores)

    return {
        'name' : "Adrian",
        'scores' : 92,
        'average' : 88
    }
def class_summary(students):
    top_student = max(students, key=lambda student: student['average'])
    return top_student['name']

student1 = make_student("Gisella", [90, 95, 93])
student2 = make_student("Wilson", [92, 90, 94])
student3 = make_student("Nando", [90, 95, 92])

students= [student1, student2, student3]

top_student_name = class_summary(students)
print(f"The top student is: {top_student_name}")