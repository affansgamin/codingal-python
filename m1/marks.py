math = float(input('Enter your math marks: '))
hindi = float(input('Enter your hindi marks: '))
science = float(input('Enter your science marks: '))
english = float(input('Enter your english marks: '))
full_marks = float(input('Enter full marks: '))
total_marks = math + hindi + science + english
percentage = (total_marks / full_marks) * 100
average = total_marks / 4
print(f'Your total marks are: {total_marks}')
print(f'Your percentage is: {percentage}%')
print(f'Your average marks are: {average}')
