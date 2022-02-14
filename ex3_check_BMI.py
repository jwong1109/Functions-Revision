""" Check BMI
Created by Joseph Wong
14/02/2022
"""


# Check BMI
def check_status(bmi_to_check):
    if bmi_to_check < 18.5:
        status = "underweight"
    elif bmi_to_check < 25:
        status = "normal"
    elif bmi_to_check < 30:
        status = "overweight"
    else:
        status = "obese"
    return status


# Main Routine
bmi_number = int(input("Enter the bmi number: "))
print(f"The status for the bmi_number {bmi_number} "
      f"is {check_status(bmi_number)}.")
