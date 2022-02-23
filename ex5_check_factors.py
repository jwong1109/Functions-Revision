""" Check for Factors
Created by Joseph Wong
15/02/2022
"""


# Function
def check_factor(num1, num2):
    if num1 % num2 == 0:
        print(f"{num2} is a factor of {num1}")
    else:
        print(f"{num2} is NOT a factor of {num1}")


# Main Routine
num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))

check_factor(num1, num2)
