start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
total_sum = 0
for num in range(start, end + 1):
    print(num)
    total_sum += num
print(f"The sum of numbers from {start} to {end} is: {total_sum}")