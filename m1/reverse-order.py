end = int(input("Enter the end of the range: "))
start = int(input("Enter the start of the range: "))
if start > end:
    print("Invalid range. Start should be less than or equal to end.")
else:
    for num in range(end, start - 1, -1):
        print(num)