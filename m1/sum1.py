while True:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    sum = 0
    while start <= end:
        # print(start)
        sum += start
        start += 1
    print(f"The sum from the start to end is: {sum}")
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() == 'y':
        continue
    elif cont.lower() == 'n':
        print("Exiting the program.")
        break
    else :
        print("Invalid input. Please enter 'y' or 'n'.")
        