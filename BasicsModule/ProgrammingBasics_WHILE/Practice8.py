# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

name = input()
grades = 1.0
sum_grades = 0.0
excluded = 0

while grades <= 12:
    grade = float(input())
    if grade < 4.00:
        excluded += 1
        if excluded > 1:
            print(f'{name} has been excluded at {grades:.0f} grade')
            break
    sum_grades += grade
    grades += 1
    if grades == 12:
        average = sum_grades / 12
        print(f'{name} graduated. Average grade: {average:.2f}')