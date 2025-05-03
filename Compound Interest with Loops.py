# Name - Derek Simons
# Class - Py
# Assignment - Compound Interest with Loops
# Date - 04/8/2025

# Inputs and Loops

while True:
    try:
        fDeposit = float(input("What is the original deposit (positive value)? "))
        if fDeposit <= 0:
            print("Input must > 0.")
            continue

        break
    except ValueError:
        print("Input must be a positive numeric value.")

while True:
    try:
        fInterest = float(input("What is the interest rate? (positive value) "))
        if fInterest <= 0:
            print("Input must > 0.")
            continue

        break
    except ValueError:
        print("Input must be a positive numeric value.")

while True:
    try:
        iMonths = int(input("What is the number of months? (positive value) "))
        if iMonths <= 0:
            print("Input must > 0.")
            continue

        break
    except ValueError:
        print("Input must be a positive numeric value.")

while True:
    try:
        fGoal = float(input("What is the goal amount? (Can enter 0 but not negative) "))
        if fGoal < 0:
            print("Input must >= 0.")
            continue

        break
    except ValueError:
        print("Input must be a positive numeric value.")

# Account Balance/output
        
fMonthInt = (fInterest / 100) / 12
fAccount = fDeposit
for iMonth in range(1, iMonths + 1):
    fAccount += fAccount * fMonthInt
    print(f"Month: {iMonth} Account balance is: ${fAccount:,.2f}")

# How many months/output
    
if fDeposit <= fGoal and fGoal > 0.0:
    iGoalMonths = 0
    while fDeposit < fGoal:
        fDeposit += fDeposit * fMonthInt
        iGoalMonths += 1
print(f"It will take {iGoalMonths} months to reach the goal of ${fGoal:,.2f}.")

    
    




