# Name - Derek Simons
# Class - Python 2
# Assignment - Inter Planetary Weights Using Dictionaries and Pickling
# Date - 03/02/2026

# 1.) What I liked about this assignment is how we have done it already
# but this time around it is a lot more complex. Looking at the code here
# compared to the first one on GitHub shows how great Prof. C is as a professor :)

# 2.) I struggled saving the history from previous entries. As the newest thing
# for this assignment, putting it into practice was difficult. Comparing this
# assignment to the examples on blackboard helped a lot but I still had difficulty
# filling in the blanks for this assignment specifically

# 3.) Overall, I did enjoy working with dictionairies and pickling concepts as
# they compliment each other very well, and in the case of saving history it
# works together like peanut butter and jelly.

# 4.) One thing I learned about this assignment is how actually looking at the
# file in notepad or anything else, it stores it in binary so it is not readable.

# Another thing I learned is how pickling HAS to be binary, if you try to write or
# read without the b after (wb, rb for example) the code will not run at all.

import pickle

#Constants
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS =  0.92
NEPTUNE = 1.12
PLUTO = 0.066

# Error handling for weight function
def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Please enter a number greater than zero.")
            else:
                return fValue
        except ValueError:
            print("Please enter a valid number.")

# Dictionary for calculating planet weights
def PlanetaryWeight(fWeight):
    PlanetaryWeightDict = { "Mercury": MERCURY,
        "Venus": VENUS,
        "Moon": MOON,
        "Mars": MARS,
        "Jupiter": JUPITER,
        "Saturn": SATURN,
        "Uranus": URANUS,
        "Neptune": NEPTUNE,
        "Pluto": PLUTO }
    fResults = {}
    for sPlanet, fGravity in PlanetaryWeightDict.items():
        fResults[sPlanet] = fGravity * fWeight
    return fResults

#Create file to store dictPlanetHistory
sFileName = "DMSPlanetaryWeights.db"

def main():
#Attempt to open file if it exist or create it if it doesn't
    try:
        with open(sFileName, "rb") as file:
            dictPlanetHistory = pickle.load(file)
    except FileNotFoundError:
            dictPlanetHistory = {}

# Input name
    while True:
        sName = input("What is your name? (enter key to quit): ")
        if sName == "":
            break
# Check if name exist already and exit loop with enter key
        while sName in dictPlanetHistory:
            print(f"{sName} already exists. Please enter a unique name")
            sName = input("What is your name? (enter key to quit): ")
            if sName == "":
                break

# Input weight + error check func
        fWeight = getFloatInput("What is your weight? ")

# Use Planet weight dictionary calculation
        fPlanetWeight = PlanetaryWeight(fWeight)

#  Store the weights
        dictPlanetHistory[sName] = fPlanetWeight

# Save entry
        with open(sFileName, "wb") as file:
            pickle.dump(dictPlanetHistory, file)

#Print out list of all weights on each planet
        print(f"{sName}, here are your weights on our Solar System's planets:")
        for sPlanet, fWeight in fPlanetWeight.items():
            print(f"{sPlanet:<25} {fWeight:>10.2f}")

# Ask user to see history and check if they enter a y or n
        while True:
            sSeeHistory = input("Would you like to see the history y/n: ").lower()
            if sSeeHistory == "y" or sSeeHistory == "n":
                break
            else:
                print("Please enter y or n.")

# If y, display the history and check to make sure there is entries
        if sSeeHistory == "y":
            if not dictPlanetHistory:
                print("No entries found.")
            else:
                for sName, fWeight in dictPlanetHistory.items():
                    print(f"{sName}, here are your weights on our Solar System's planets: ")
                    for sPlanet, fWeight in fPlanetWeight.items():
                        print(f"{sPlanet:<25}: {fWeight:>8.2f}")

main()