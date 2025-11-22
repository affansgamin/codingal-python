char = input("Enter any character: ")

if len(char) == 1:
    print(f"The ASCII value of '{char}' is {ord(char)}")
else:
    print("Please enter only a single character.")

if ord(char) >= 48 and ord(char) <= 57:
    print(f"'{char}' is a digit.")
elif (ord(char) >= 65 and ord(char) <= 90):
    print(f"'{char}' is an uppercase alphabet.")
elif ord(char) >= 97 and ord(char) <= 122:
    print(f"'{char}' is a lowercase alphabet.")
else: 
    print(f"'{char}' is a special character.")