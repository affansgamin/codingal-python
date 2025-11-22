gb = int(input("Enter the mobile data in GB used: "))
if gb <= 5:
    cost = 100
elif gb >= 6 and gb <= 10:
    cost = 100 + (gb - 5)*20
elif gb >= 11:
    cost = 100 + (gb - 10)*30 + 5*20
print(f"The total mobile data cost is: ${cost}")
