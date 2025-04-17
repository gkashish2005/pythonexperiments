# NAME: KASHISH GUPTA 231P081/09 SE COMPS A
"""Aim: Write a program in Python to demonstrate a user-defined exception.
(Month number is input between 1-12, above 12 is an exception)."""
# User-defined exception
class InvalidMonthError(Exception):
    pass
def check_month(month):
    if month < 1 or month > 12:
        raise InvalidMonthError("Month must be between 1 and 12.")
try:
    month = int(input("Enter month number (1-12): "))
    check_month(month)
    print(f"Month {month} is valid.")
except InvalidMonthError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")
print("\nThank You \nName: KASHISH GUPTA \nUIN: 231P081 \nRoll no: 09 \n")
