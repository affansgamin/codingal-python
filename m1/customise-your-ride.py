vehicle = input("Enter the type of vehicle car or bike (a/b): ")
if vehicle == 'a':
    print("You have selected a car.")
    car_type = input("Enter the type of car sedan or suv (s/u): ")
    if car_type == 's':
        print("You have selected a sedan.")
    elif car_type == 'u':
        print("You have selected an SUV.")
    else:
        print("Invalid car type selected.")
elif vehicle == 'b':
    print("You have selected a bike.")
    bike_type = input("Enter the type of bike sports or cruiser (s/c): ")
    if bike_type == 's':
        print("You have selected a sports bike.")
    elif bike_type == 'c':
        print("You have selected a cruiser bike.")
    else:
        print("Invalid bike type selected.")
else:
    print("Invalid vehicle type selected.")