# Name - Derek Simons
# Class - Py
# Assignment - Paint Job with Functions and Output Files
# Date - 4/26/25

# Math Function

from math import ceil

#Functions

def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                raise ValueError
            return fValue
        except ValueError:
            print("Enter number > 0.")

def getGallonsOfPaint(fSquareFeet, fFtPerGallon):
    return ceil(fSquareFeet / fFtPerGallon)

def getLaborHours(fHoursPerGallon, iTotalGallons):
    return fHoursPerGallon * iTotalGallons

def getLaborCost(fHoursPerGallon, fLaborPerHour):
    return fHoursPerGallon * fLaborPerHour

def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

def getSalesTax(sState):
    if sState == 'VT' or sState == 'CT':
        return 0.06
    elif sState == 'MA':
        return 0.0625
    elif sState == 'ME':
        return 0.0085
    elif sState == 'RI':
        return 0.07
    elif sState == 'NH':
        return 0.0
    else:
        return 0.0

def showCostEstimate(iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fTaxRate, sName):
    fTotalLaborCost = fLaborCost * iTotalGallons
    fTaxAmount = fTaxRate * (fTotalLaborCost + fPaintCost)
    fTotalCost = fTotalLaborCost + fPaintCost + fTaxAmount
    sFileName = f"{sName}_PaintJobOutput.txt"

#Output
    
    print(f"Gallons of paint: {iTotalGallons}")
    print(f"Hours of labor: {fLaborHours}")
    print(f"Paint charges: ${fPaintCost:.2f}")
    print(f"Labor charges: ${fTotalLaborCost:,.2f}")
    print(f"Tax: ${fTaxAmount:.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")

#File
    
    with open(sFileName, "w") as f:
        f.write(f"Customer: {sName}\n")
        f.write(f"Gallons of paint: {iTotalGallons} gallons\n")
        f.write(f"Hours of labor: {fLaborHours} hours\n")
        f.write(f"Paint charges: ${fPaintCost:.2f}\n")
        f.write(f"Labor charges: ${fTotalLaborCost:,.2f}\n")
        f.write(f"Tax: ${fTaxAmount:.2f}\n")
        f.write(f"Total cost: ${fTotalCost:,.2f}")

    print(f"File: {sFileName} was created.")

def main():

# Input

    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fHourlyRate = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ").upper()
    sName = input("Customer's last name: ").title()

    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fHoursPerGallon, fHourlyRate)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fTaxRate = getSalesTax(sState)

    showCostEstimate(iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fTaxRate, sName)

main()
        
