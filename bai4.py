def sort_by_math_and_literature_score(arr):
    sorted_list = sorted(arr, key=lambda x: (x["math"], x["literature"]), reverse=True)
    return sorted_list

student_grade_list = [
    {'id': 984, 'math': 9, 'literature': 5},
    {'id': 12, 'math': 10, 'literature': 4},
    {'id': 324, 'math': 10, 'literature': 5},
    {'id': 890, 'math': 5, 'literature': 7},
    {'id': 223, 'math': 8, 'literature': 8},
    {'id': 543, 'math': 8, 'literature': 5},
]

sorted_student_list = sort_by_math_and_literature_score(student_grade_list)

for student in sorted_student_list:
    print(f"Học sinh {student['id']}: Toán {student['math']}, Văn {student['literature']}")