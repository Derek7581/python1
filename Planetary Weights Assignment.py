# Name- Derek Simons
# Class- Py
# Project- Planetary Weights
# Date- 02/22/2025

#CONSTANTS

'MERCURY' == 0.38
'VENUS' == 0.91
'MOON' == 0.165
'MARS' == 0.38
'JUPITER' == 2.34
'SATURN' == 0.93
'URANUS' == 0.92
'NEPTUNE' == 1.12
'PLUTO' == 0.066

#Inputs

sName = input("What is the your name? ")
fWeight = float(input("How much do you weigh? "))
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN= 0.93
URANUS= 0.92
NEPTUNE= 1.12
PLUTO= 0.066


#Calculations

fMercury = fWeight * MERCURY
fVenus = fWeight * VENUS
fMoon = fWeight * MOON
fMars = fWeight * MARS
fJupiter = fWeight * JUPITER
fSaturn = fWeight * SATURN
fUranus = fWeight * URANUS
fNeptune = fWeight * NEPTUNE
fPluto = fWeight * PLUTO

#Output

print (f"On Mercury, you weigh:           {fMercury:.2f}")
print (f"On Venus, you weigh:             {fVenus:.2f}")
print (f"On Mars, you weigh:              {fMars:.2f}")
print (f"On Jupiter, you weigh:           {fJupiter:.2f}")
print (f"On Saturn, you weigh:            {fSaturn:.2f}")
print (f"On Uranus, you weigh:            {fUranus:.2f}")
print (f"On Neptune, you weigh:           {fNeptune:.2f}")
print (f"On Pluto, you weigh:             {fPluto:.2f}")
