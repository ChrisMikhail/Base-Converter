# This program takes any number from any base and converts it into any number in another base.
# However, if the user enters a number that cant be represented in that certain base;
# they will be prompted to re-enter a valid number. (ex the digit 3 doesn't exist in base 2.)


def introduce_program():

    # prints out the program introduction to the user.
    print("Welcome, this program will convert any whole number from one base into another (Up to base 16).")


def get_base_input(prompt):

    # returns the first and second base entered by the user.
    base = int(input(prompt)) # prompt changes based off which base we are asking for (1 or 2)
    return base


def get_num_input():

    # Asks the user for a number which will be converted later
    UserNum = input("Please enter a number: ")
    return UserNum # Returns the number that the user inputted


def check_in_base(StrInput, base):

    # Checks to see if the inputted number is in the range of the first base entered
    for i in range(len(StrInput)): # Loop that iterates as long as the number entered by the user
        if hex_to_value(StrInput[i]) >= base: # Checks to see if input is greater or equal to the original base
            return True # Returns true if a value entered by the user isnt within the base


def hex_to_value(hexDigit):

    # Converts hex values beyond 9 (A to F) to their respective decimal values
    hexDigits = "0123456789ABCDEF" # String containing every possible digit from base 1 to base 16
    for i in range(len(hexDigits)): # Loops through every base hex digit
        if hexDigits[i] == hexDigit: # Identifies if any hex values are in the user's number
            return i # returns the index of that and assigns that value for the number


def value_to_hex(hexDigit):

    # Converts numbers past 10 into their respective hexadecimal representations
    hexDigits = "0123456789ABCDEF" # String of all digits in hex
    for x in range(len(hexDigits)): # Loop that iterates through every digit
        if int(hexDigit) == x: # Checks if the user input has a hex representation based off position
            return hexDigits[x] # Returns the hex digit associated with the numerical value from input


def convert_num(userNumStr, firstBase, secondBase):

    # Converts numbers from base 10, and then to another base if needed
    DecimalRep = 0 # Decimal representation of a number. Will change based off input
    remainder = [] # List that temporarily holds values of for the conversion
    convertedNum = ""
    for i in range(len(userNumStr) - 1, -1, -1): # Loop that iterates backwards
        DecimalRep += hex_to_value(userNumStr[i]) * (firstBase ** (len(userNumStr) - i - 1))
        # Converts user input into base 10
        # Done by adding the digit and multiplying it by the first base to the power of its significance
    while DecimalRep >= 1: # Loops until the base 10 number has no remainder left
        remainder.append(DecimalRep % secondBase) # Adds the remainder of the base 10 number divided by base 2 to the
        # list
        DecimalRep = DecimalRep // secondBase # Updates value of DecimalRep to be the closest whole number of
        # DecimalRep divided by base 2
        newNum = str(remainder.pop()) # Removes values from the list and adds it to a string containing all the values
        convertedNum += value_to_hex(newNum) # Converts numbers to their hex values if applicable
    return convertedNum[::-1] # Returns the flipped version of the converted number


def print_statements(num, base, Secondbase, finalAnswer, checkthebase):
    while checkthebase: # Loops until the user enters a valid input
        print("That number does not exist in base", base) # Statement indicating to the user to re=enter a number
        num = get_num_input()
        base = get_base_input("What base is your number in? ")
        checkthebase = check_in_base(num, base)
        Secondbase = get_base_input("What base will your number be converted into? ")
        finalAnswer = convert_num(num, base, Secondbase)
    # Prints the final print statement.
    # Including the original number, first and second base and the final answer
    print("When converting", num, "from base", base, "to base", str(Secondbase) + ", the result is:", finalAnswer)

if __name__ == "__main__":
    num = get_num_input()
    base1 = get_base_input("What base is your number in? ")
    checkBase = check_in_base(num, base1)
    base2 = get_base_input("What base will your number be converted into? ")
    finalNumber = convert_num(num, base1, base2)
    print_statements(num, base1, base2, finalNumber, checkBase) # Prints conversion and input validation if needed
