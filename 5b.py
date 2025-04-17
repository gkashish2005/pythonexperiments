# NAME: KASHISH GUPTA 2E31P081/09 SE COMPS A
""" WAP to create a user-defined exception where the program will ask the user
to input a number again and again until the user enters the correct stored number."""
# User-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass
# Define class for NegativeValueError
class NegativeValueError(Error):
    """Raised when the input is negative"""
    pass
# Define class for ValueTooSmallError
class ValueTooSmallError(Error):
    """Raised when the value is too small"""
    pass
# Define class for ValueTooLargeError
class ValueTooLargeError(Error):
    """Raised when the value is too large"""
    pass
# Main program
# Takes input till the user inputs the correct value
# Stored number
number = 11
while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegativeValueError
        elif num < number:
            raise ValueTooSmallError
        elif num > number:
            raise ValueTooLargeError
        break
    except NegativeValueError:
        print("This is a negative value, try again\n")
    except ValueTooSmallError:
        print("This value is too small, try again\n")
    except ValueTooLargeError:
        print("This value is too large, try again!\n")
print("Correct value entered")
print("\nThank You \nName: KASHISH GUPTA \nUIN:231P081 \nRoll no:09 \n")
