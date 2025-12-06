number = int(input("Enter a number: "))
power = int(input("Enter the power to raise the number to: "))

result = 1
count = 0

while count < power:
    result = result * number
    count = count + 1

print(f"{number} raised to the power of {power} is {result}")