name_marks = {"Rohan":80,"Meena":88,"Pooja":100,"Ram":85,"Divya":97}
sum_marks = 0
max_marks = max(name_marks.values())
min_marks = min(name_marks.values())
max_name = ''
min_name = ''
for i in name_marks.values():
    sum_marks+=i
try:
    avg = sum_marks//len(name_marks)
except ZeroDivisionError:
    print('Division by zero(0)is not possible!')
for j in name_marks.keys():
    if name_marks[j] == max_marks:
        max_name = j
for k in name_marks.keys():
    if name_marks[k] == min_marks:
        min_name = k
print(max_name,'scored the highest marks of',max_marks)
print(min_name,'scored the lowest marks of',min_marks)
try:
    student_choice_seemarks = input('Enter the students name: ')
except ValueError:
    print('Enter a name, not anything else!')
student_name = name_marks.get(student_choice_seemarks)
name_not_found_message = 'Not Found!'
if student_choice_seemarks not in name_marks.keys():
    print(name_not_found_message)
else:
    print('The student scored',student_name,'marks')
print('The average of all students is',avg)