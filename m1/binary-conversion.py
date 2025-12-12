decimal_num = int(input("enter a decimal number: "))
binary_num = ""
while decimal_num >0:
    remainder = decimal_num%2
    binary_num = str(remainder)+ binary_num
    decimal_num//=2
print(f"your binary number is: {binary_num}")