char = input("Enter any character: ")

if len(char) == 1:
    print(f"The ASCII value of '{char}' is {ord(char)}")
else:
    print("Please enter only a single character.")