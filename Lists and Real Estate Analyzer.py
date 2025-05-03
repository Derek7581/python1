# Name - Derek Simons
# Class - Py
# Assignment - Lists and Real Estate Analyzer
# Date - 4/30/2025

#Float Function

def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Input a number > 0.")
                continue
            return fValue
        except ValueError:
            print("Input a number that is greater than 0.")

#Median Function
            
def getMedian(sListSales):
    fListLength = len(sListSales)
    
    if fListLength % 2 == 0:
        fMiddle1 = fListLength // 2
        fMiddle2 = fMiddle1 - 1
        return (sListSales[fMiddle1] + sListSales[fMiddle2]) / 2
    else:
        fMiddle3 = fListLength // 2
        return sListSales[fMiddle3]

def main():

#List Loop
    
    sListSales = []

    while True:
            sListSales.append(getFloatInput("Enter property sales tax: "))
            
            sAdd = input("Enter another value? ( Y or N ): ").upper()
            if sAdd == 'Y':
                continue
            elif sAdd == 'N':
                break
            else:
                print("Please enter a Y or N")
            continue

#Organize Loop
    
    sListSales.sort()

#Calculations

    fMin = sListSales[0]

    fMax = sListSales[-1]

    fTotal = sum(sListSales)

    iCount = len(sListSales)

    fAverage = fTotal / iCount

    fCommission = fTotal * 0.03

    fMedian = getMedian(sListSales)

#Output
    
    for sSale in range(0, iCount):
        print(f"Property {sSale + 1}: ${sListSales[sSale]:,.2f}")

    print(f"Minimum: ${fMin:,.2f}")
    print(f"Maximum: ${fMax:,.2f}")
    print(f"Total: ${fTotal:,.2f}")
    print(f"Average: ${fAverage:,.2f}")
    print(f"Median: ${fMedian:,.2f}")
    print(f"Commission: ${fCommission:,.2f}")
    
main()











    
