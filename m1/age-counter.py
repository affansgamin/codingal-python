age = int(input('Enter your age: '))
try:
    if age <18:
        raise ValueError
    else:
        if age %2 ==0:
            print(f'Success! The age {age} is an even number')
        else: print(f'Success! The age {age} is an odd number')
except ValueError:
    print('invalid age')