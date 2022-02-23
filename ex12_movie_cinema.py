""" Movie Cinema
Created by Joseph Wong
18/02/2022
"""


# Type of ticket function
def ticket_type():
    type_ = str(input("What type of ticket do you want?\nA for Adult, or\n "
                      "S for Student, or\nC for Child, or\n"
                      "G for Gift Voucher\n >> "))
    confirm = input(f"Confirm purchase of {type_} ticket? (Y/N): ")
    if confirm == "Y":
        return type_
    else:
        return "Cancelled"


# Main Routine
adult = 0
student = 0
child = 0
gift = 0
tickets_sold = 0
sell_ticket = input("Do you want to sell a ticket? (Y/N): ")
while sell_ticket != "N":
    type = ticket_type()
    if type == "A":
        adult += 1
        tickets_sold += 1
    elif type == "S":
        student += 1
        tickets_sold += 1
    elif type == "C":
        child += 1
        tickets_sold += 1
    elif type == "G":
        gift += 1
        tickets_sold += 1
    else:
        print("Purchase cancelled!")
    sell_ticket = input("Do you want to sell another ticket? (Y/N): ")
print("==================")
print(f"The total tickets sold today was {tickets_sold}")
print("This was made of:")
print(f"{adult} for adults; and\n{student} for students; and"
      f"\n{child} for children; and\n{gift} for gift vouchers")
ADULT_COST = 12.5
STUDENT_COST = 9
CHILD_COST = 7
GIFT_COST = 0
total_sales = adult * ADULT_COST + student * STUDENT_COST + child * CHILD_COST
print(f"Sales for the day came to ${total_sales:,.2f}")
