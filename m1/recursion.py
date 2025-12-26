def sub(a, b = 0):
    result = a - b
    print(result)
    if result>0:
        sub(result, 2)
        
    print('end of sub function')
    
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

sub(a, b) 