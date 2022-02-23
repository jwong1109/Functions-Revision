""" Find Multiples
Created by Joseph Wong
15/02/2022
"""


# Function
def find_multiples(num_list, factor):
    multiples = []
    for i in num_list:
        if i % factor == 0:
            multiples.append(i)
    return multiples


# Main Routine
num_list = [1, 4, 6, 7, 15, 22, 35]
print(find_multiples(num_list, 5))
print(find_multiples(num_list, 2))
