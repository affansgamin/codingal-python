list1 = []
def create_list():
    size = int(input('enter how many students: '))
    sum = 0
    for i in range(size):
        marks = int(input(f'enter marks for student {i+1}: '))
        list1.append(marks)
    print(f'students marks are: {list1}')
def add_single():
    new_mark = int(input('enter the new mark: '))
    list1.append(new_mark)
    print(f'students marks are: {list1}')
def add_multiple():
    list2 = [int(x) for x in input("Enter integers separated by spaces: ").split()]
    list1.extend(list2)
    print(f'students marks are: {list1}')
def sort_list():
    list1.sort()
    print(f'sorted list is: {list1}')
def reverse_list():
    list1.reverse()
    print(f'reversed list: {list1}')
def remove_single():
    discarded_mark = int(input('enter mark to remove: '))
    list1.remove(discarded_mark)
    print(f'after removing {discarded_mark}: {list1}')
def find_max():
    print(f'maximum mark is: {max(list1)}')
def find_min():
    print(f'minimum mark is: {min(list1)}')
while True:
    print('0. exit program,\n 1. create list,\n 2.add single,\n 3. add multiple,\n 4. sort,\n 5. reverse,\n 6. remove single,\n 7. find max, \n 8. find minimum')
    choice = int(input('Enter your choice (0, 1, 2, 3, 4, 5, 6, 7, 8): '))
    if choice == 1:
        create_list()
    elif choice == 2:
        add_single()
    elif choice == 3:
        add_multiple()
    elif choice == 0:
        print('exiting the program')
        exit()
    elif choice == 4:
        sort_list()
    elif choice == 5:
        reverse_list()
    elif choice == 6:
        remove_single()
    elif choice == 7:
        find_max()
    elif choice == 8:
        find_min()
    else:
        print('invalid input')