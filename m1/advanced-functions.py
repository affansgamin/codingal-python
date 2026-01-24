def find_cube(n):
    return n*n*n

list1 = []
length = int(input('Enter the length: '))
for i in range(length):
    value = int(input('Enter a value: '))
    list1.append(value)
print(f'original list: {list1}')
list_div_3 = [i for i in list1 if i%3 == 0]
print(f'list divisible by 3: {list_div_3}')
cube_list = list(map(find_cube, list_div_3))
print(f'cubed list is: {cube_list}')
zipped = list(zip(list_div_3, cube_list))
print(zipped)
myDict = {str(x): x**3 for x in list_div_3}
print(myDict)