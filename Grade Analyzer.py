# Name - Derek Simons
# Class - Py
# Assignment - Grade Analyzer
# Date - 3/26/25

#Input Name

sName = input("Who is being graded? ")

#Input Scores

iTest1 = int(input("What is test score 1? "))

iTest2 = int(input("What is test score 2? "))

iTest3 = int(input("What is test score 3? "))

iTest4 = int(input("What is test score 4? "))

if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()

#Input Drop Low Score
    
sDrop = input("Would you like to drop the lowest score (Y/N)? ").lower()


#Dropped Score

if sDrop == 'n':
    fTestAvg = (( iTest1 + iTest2 + iTest3 + iTest4 ) / 4.0)
elif sDrop == 'y':
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fTestAvg = (iTest2 + iTest3 + iTest4 ) / 3.0
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        fTestAvg = ( iTest1 + iTest3 + iTest4 ) / 3.0
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        fTestAvg = ( iTest1 + iTest2 + iTest4 ) / 3.0
    else:
        fTestAvg = ( iTest1 + iTest2 + iTest3 ) / 3.0
else:
    print("Please enter Y/N")
    exit()

#Grade Analyzer

if fTestAvg >= 97.0:
    sGrade = "A+"
elif fTestAvg >= 94.0:
    sGrade = "A"
elif fTestAvg >= 90.0:
    sGrade = "A-"
elif fTestAvg >= 87.0:
    sGrade = "B+"
elif fTestAvg >= 84.0:
    sGrade = "B"
elif fTestAvg >= 80.0:
    sGrade = "B-"
elif fTestAvg >= 77.0:
    sGrade = "C+"
elif fTestAvg >= 74.0:
    sGrade = "C"
elif fTestAvg >= 70.0:
    sGrade = "C-"
elif fTestAvg >= 67.0:
    sGrade = "D+"
elif fTestAvg >= 64.0:
    sGrade = "D"
elif fTestAvg >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F, learn to RTFS"

#Output

print(f"{sName}'s test average is {fTestAvg:.1f}.")
print(f"{sName}'s grade is {sGrade}.")


