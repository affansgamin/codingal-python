number = int(input('Enter a number: '))
if number % 2 == 0:
    print(f'The number {number} is even.')
    if number % 3 == 0:
        print(f'The number {number} is divisible by 3.')
    else:
        print(f'The number {number} is not divisible by 3.')
else:
    print(f'The number {number} is odd.')
