medical_cause = input("Is there a medical cause for the exam? (y/n): ")
if medical_cause == 'y':
    print("You are eligible to sit for the exam due to medical reasons.")

else:
    attendance_percentage = int(input("Enter your attendance percentage: "))
    

    if attendance_percentage <= 74:
        print("You are not eligible to sit for the exam due to low attendance.")
    else:
        print("You are eligible to sit for the exam.")
