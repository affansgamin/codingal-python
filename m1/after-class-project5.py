char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    ascii_value = ord(char)
    
    if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is NOT an alphabet.")