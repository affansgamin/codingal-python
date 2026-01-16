n1 = int(input('Enter the first number:'))
n2 = int(input('Enter the last number:'))
og_list = []
square_list = []
even_list = []
odd_list = []
for i in range(n1, n2+1):
    og_list.append(i)
print(f'original list: {og_list}')
for i in og_list:
    square = i*i
    square_list.append(square)
print(f'squared list: {square_list}')
even_list = [i for i in square_list if i%2 == 0]
print(f'Even list: {even_list}')
odd_list = [i for i in square_list if i%2 == 1]
print(f'Odd list: {odd_list}')