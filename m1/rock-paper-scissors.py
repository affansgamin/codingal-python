import random
user_choice = input('Enter rock, paper or scissors: ')
options = ['rock', 'paper', 'scissors']
com_choice = random.choice(options)
if user_choice not in options:
    print('invalid input, try again')
print(f'You chose: {user_choice}')
print(f'Computer chose: {com_choice}')
if user_choice == com_choice:
    print('tie')
elif (user_choice == 'rock' and com_choice == 'scissors') or (user_choice == 'paper' and com_choice == 'rock') or (user_choice == 'scissors' and com_choice == 'paper'):
    print('You win')
else:
    print('Computer wins')