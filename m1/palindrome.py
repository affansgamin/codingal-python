def checkPalindrome(og_tuple):
    rev_tuple = og_tuple[::-1]
    print(f'Reversed tuple: {rev_tuple}')
    if rev_tuple == og_tuple:
        print('tuple is a palindrome')
    else:
        print('tuple is not a palindrome')
def takeInput(length):
    og_list = []
    for i in range(length):
        element = int(input('Enter element: '))
        og_list.append(element)
    og_tuple = tuple(og_list)
    checkPalindrome(og_tuple)


length = int(input('enter the length of the tuple: '))
takeInput(length)