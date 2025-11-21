grade = float(input("Enter your grade: "))
if grade >= 94:
    print("Your letter grade is: A")
elif grade >= 90:
    print("Your letter grade is: A-")
elif grade >= 87:
    print("Your letter grade is: B+")
elif grade >= 83:
    print("Your letter grade is: B")
elif grade >= 80:
    print("Your letter grade is: B-")
elif grade >= 77:
    print("Your letter grade is: C+")  
elif grade >= 73:
    print("Your letter grade is: C")
elif grade >= 70:
    print("Your letter grade is: C-")
elif grade >= 67:
    print("Your letter grade is: D+")  
elif grade >= 60:
    print("Your letter grade is: D")
elif grade >= 0:
    print("Your letter grade is: F")
else:
    print("Invalid grade entered.")
