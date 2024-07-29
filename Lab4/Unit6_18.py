grades = {'Alice': [85, 90, 92], 'Bob': [88, 87, 85],'Charlie': [90, 91, 89]}
average_grades = {}
    #(key)   #(value)
for student, grade_list in grades.items():
    average_grades[student] = sum(grade_list) / len(grade_list)#len คือ ความยาวในที่นี้คือ 3

print("Average Grades: ", average_grades)