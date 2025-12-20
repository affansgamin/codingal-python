def add(n, n2):
    return n + n2
def subtract(n, n2):
    return n - n2
def divide(n, n2):
    return n / n2
def multiply(n, n2):
    return n * n2
def mod(n, n2):
    return n %n2
def exp(n, n2):
    return n ** n2
while True:
    n = int(input("enter the first number: "))
    n2 = int(input("enter the second number: "))
    print('0. quit')
    print('1. add')
    print('2. subtract')
    print('3. divide')
    print('4. multiply')
    print('5. mod')
    print('6. exponentiation') 

    option = int(input("please choose an option from 0-6 : "))

    if option == 0:
        print('exiting the program...')
        break
    elif option == 1:
        print(f'sum = {add(n, n2)}')
        break
    elif option == 2:
        print(f'subtraction = {subtract(n, n2)}')
        break
    elif option == 3:
        print(f'division = {divide(n, n2)}')
        break
    elif option == 4:
        print(f'multiplication = {multiply(n, n2)}')
        break
    elif option == 5:
        print(f'mod = {mod(n, n2)}')
        break
    elif option == 6:
        print(f'exponentiation = {exp(n, n2)}')
        break
    else:
        print('invalid input')
        break