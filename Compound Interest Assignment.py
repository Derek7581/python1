#Name- Derek Simons
#Class- Py
#Assignment- Compound Interest
#Date- 02/27/2025

#CONSTANTS

PERCENT = 100

#Input

fStart = float(input("Enter the starting principal: "))
fInterest = float(input("Enter the annual rate: "))
fStatedRate = fInterest / PERCENT
fCompound = float(input("How many times per year is the interest compounded? "))
fYears = float(input("For how many years will the account earn interest? "))

#Calculations

fDivision = fStatedRate / fCompound
fMultiply = fYears * fCompound
fExponent = (1 + fDivision) ** fMultiply
fFinal = fStart * fExponent

#Output

print(f"At the end of the {fYears} years, you will have ${fFinal: .2f}") 
