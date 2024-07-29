grades = {'Aliec': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}

print("Bob's grade:", grades['Bob'])

grades['Eve'] = 90

for student, grade in grades.items():
    print(f"{student}: {grade}")

print("Frank's grade: ",grades.get('Frank', 'Grade not found'))