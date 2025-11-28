gb = int(input("Enter the mobile data in GB used: "))
if gb <= 5:
    cost = 100*gb
elif gb >= 6 and gb <= 10:
    cost = 100*5 + (gb - 5)*120
elif gb >= 11:
    cost = 100*5 + 120*5 + (gb - 10)*130
print(f"The total mobile data cost is: ${cost}")
