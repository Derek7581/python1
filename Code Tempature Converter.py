#Name- Derek Simons
#Class- Py
#Assignment- Code Tempature Converter
#Date- 03/05/2025

#Constants


#Input

sName= input("What is your name?")
fTemp= float(input(f"Welcome {sName}, what is the tempature? "))
sConversion= input("Is the temp F for Farenheit or C for Celsius? ")

#Calculation

Celsius = float((5.0/9) * (fTemp - 32))
    
Farenheit = float(((9.0/5.0) * fTemp) + 32)

#Output

if sConversion == ("C" or "c") and fTemp > 100:
    print("Temp cannot be > 100.")
elif sConversion == ("C" or "c") and fTemp < 100:
    print(f"The Farenheit equivalent is {Farenheit:.1f}.")
elif sConversion == ("F" or "f") and fTemp > 212:
    print("Temp cannot be > 212.")
elif sConversion == ("F" or "f") and fTemp < 212:
    print(f"The Celsius equivalent is {Celsius:.1f}.")
else:
    print("You must enter F or C")



    




    

    

    
    

