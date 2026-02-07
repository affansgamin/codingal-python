size = int(input('enter how many subjects: '))
list1 = []
sum = 0
for i in range(size):
    marks = float(input('enter marks: '))
    list1.append(marks)
print(f'your marks are: {list1}')
for i in list1:
    sum += i
print(f'total marks: {sum}')
average = sum/size
print(f'average marks per subject: {average}')
