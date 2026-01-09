list1 = [3, 4, 6]
list2 = [1, 2, 3, 2, 1]
list3 = list1 + list2
print(list3)
list4 = list3
list3.reverse()
print(f'reversed list is: {list3}')
list3.sort()
print(f'sorted list is: {list3}')
length = len(list3)
print(f'length of the list it {length}')
key = int(input('enter key: '))
print(f'{key} has appeared in the list {list3.count(key)} times')
sum = 0
print(list4)
for i in list3:
    sum += i
print(f'sum of the list is: {sum}')