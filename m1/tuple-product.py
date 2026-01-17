def tuple_multiply(length):
    og_list = []
    result = 1
    for i in range(length):
        element = int(input('Enter a number: '))
        result*= element
        og_list.append(element)
    og_tuple = tuple(og_list)
    print(f'the tuple is: {og_tuple}')
    print(f'product of the tuple is: {result}')

length = int(input('Enter the length of the tuple: '))
tuple_multiply(length)