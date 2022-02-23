""" Calculate GST
Created by Joseph Wong
17/02/2022
"""


# Function
def calc_gst(net_price_):
    return net_price_ * 1.15


# Main Routine
net_price = float(input("Enter the net price: "))
print(f"${(calc_gst(net_price)):,.2f}")
