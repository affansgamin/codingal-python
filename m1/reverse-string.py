str1 = input("Enter a string: ")
reversed_str = ""
for i in str1:
    reversed_str = i + reversed_str
print("Original string is:", str1)
print("Reversed string is:", reversed_str)