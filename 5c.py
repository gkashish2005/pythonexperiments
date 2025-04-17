# NAME: KASHISH GUPTA 231P081/09 SE COMPS A
"""Aim: Write a program in Python that validates names and age as entered by the user
to determine whether the person can cast a vote or not using exception handling."""
def validate_name(name):
    if not name.isalpha():
        raise ValueError("Name must contain only letters.")
def validate_age(age):
    if age <= 0:
        raise ValueError("Age must be a positive number.")
    if age < 18:
        raise ValueError("You must be at least 18 years old to vote.")
try:
    name = input("Enter your name: ")
    validate_name(name)  # Validate the name
    age = int(input("Enter your age: "))
    validate_age(age)  # Validate the age
    # Check if eligible to vote
    if age >= 18:
        print(f"Hello {name}, you are eligible to vote!")
    else:
        print(f"Hello {name}, you are not eligible to vote!")
except ValueError as e:
    print(f"Error: {e}")
print("\nThank You \nName: KASHISH GUPTA \nUIN: 231P081 \nRoll no: 09 \n")
