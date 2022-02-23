""" Overdue Fines
Created by Joseph Wong
17/02/2022
"""


# Function
def calc_overdue(overdue):
    BASE = 0.5
    DAY = 0.8
    MAX_CHARGE = 30
    total = BASE + overdue * DAY
    if total < MAX_CHARGE:
        return total
    else:
        return MAX_CHARGE


# Main Routine
days_overdue = int(input("Enter days overdue: "))
print(f"Fine is ${calc_overdue(days_overdue):,.2f}")
