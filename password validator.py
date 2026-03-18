#Name - Derek Simons
#Class - Python 2
#Assignment - Password Validator
#Date - 02/09/26 - 02/21/26

#Reflection:
#1.) What I liked about this assignment is the real world factor of it.
#I am interested in a career in cybersecurity so making sure users are providing strong passwords seems relevant.

#2.) I struggled mainly with making sure there is no repeating characters.
#Listing out what was repeated and how many times took a lot of time of trial and error.
#But that's how we learn.

#3.) I made the code efficient by using built-in string functions from Python.
#Such as .islower(), .isupper, ect.
#Two things I've learned from this assignment is the value of dictionaries.
#Like how they can be utilized to define certain things through the key-value setup.
#And to utilize that to check for specific criteria.
#Another thing I learned is that it is better to use .lower() in most scenarios rather than .upper().
#Since most characters we type end up being lowercase it saves Python a little bit of time.

#Defining dictionary function
def PasswordValidator(sPassword):
    DictPass = { "bUpper": False,
        "bLower": False,
        "bDigit": False,
        "bSpecial": False }

    #Confirm if password meets character requirements
    for char in sPassword:
        if char.isupper():
            DictPass["bUpper"] = True
        elif char.islower():
            DictPass["bLower"] = True
        elif char.isdigit():
            DictPass["bDigit"] = True
        elif char in "!@#$^":
            DictPass["bSpecial"] = True
    return DictPass

def main():
    # Prompt user for name
    sNameDMS = input("What is your first and last name? ")

    # Extract initials
    sFirstInitial = sNameDMS.lower()[0]
    sFirstAndLast = sNameDMS.split()
    sLastInitial = sFirstAndLast[-1].lower()[0]
    sInitialDMS = sFirstInitial + sLastInitial

    #Input password and loop
    while True:
        sPasswordDMS = input("Enter a password: ")
        #Use dictionary function
        DictTest = PasswordValidator(sPasswordDMS)
        #Find out length of password
        iPassword = len(sPasswordDMS)
        #Assume password is valid (until the if statement proves otherwise)
        bValidPassword = True

        #Count for repeating characters
        CharDict = {}
        for char in sPasswordDMS.lower():
            if char in CharDict:
                CharDict[char] += 1
            else:
                CharDict[char] = 1

        #Test if there is repeating characters and inform what repeated and how many times
        for char, count in CharDict.items():
            if count > 1:
                print("This character appears more than once:")
                print(f"{char}: {count} times")
                bValidPassword = False

        #Make sure password has correct amount of characters
        if iPassword < 8 or iPassword > 12:
            print("Password must be between 8 and 12 characters")
            bValidPassword = False

        #Make sure password does not start with 'pass'
        if sPasswordDMS.lower().startswith("pass"):
            print("Password can't start with 'pass'")
            bValidPassword = False

        #Make sure password does not have initials in it
        if sInitialDMS in sPasswordDMS.lower():
            print("Password must not contain initials")
            bValidPassword = False

        #Confirm if password meets requirements via PasswordValidator dictionary
        #At least one uppercase:
        if not DictTest["bUpper"]:
            print("Password must contain at least one uppercase letter")
            bValidPassword = False

        #At least one lower case:
        if not DictTest["bLower"]:
            print("Password must contain at least one lowercase letter")
            bValidPassword = False

        #At least one numerical value:
        if not DictTest["bDigit"]:
            print("Password must contain at least one digit")
            bValidPassword = False

        #At least one special character
        if not DictTest["bSpecial"]:
            print("Password must contain at least one of these special characters: ! @ # $ ^")
            bValidPassword = False

        #Break or repeat loop
        if bValidPassword == True:
            print("Password is valid and ok to use")
            break
        else:
            print("Password must meet requirements, try again")
            continue
main()






