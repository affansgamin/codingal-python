list1 = []
length1 = int(input('enter the length:'))
for i in range(length1):
    value = int(input('enter a value: '))
    list1.append(value)
    
set1 = set(list1)
print(f'list1: {list1}, set1: {set1}')