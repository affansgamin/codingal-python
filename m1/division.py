try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    result = num1/num2
    print('Result is:', result)
    print('Result is:', result1)
except ZeroDivisionError:
    print('Division by zero is not possible')
except ValueError:
    print('Enter a valid number')
except NameError as ex:
    print('The exception is', ex)
except:
    print('an error has occurred')
finally:
    print('This code will run no matter what')