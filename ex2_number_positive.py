""" Make Numbers Positive
Created by Joseph Wong
14/02/2022
"""


# Making number positive function
def make_positive(change_num):
    abs_value = abs(change_num)
    return abs_value


# Main Routine
number = int(input("Enter number: "))
print(f"The abs of {number} is {make_positive(number)}.")
