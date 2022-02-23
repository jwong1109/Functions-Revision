""" Print Strings A Number of Times
Created by Joseph Wong
15/02/2022
"""


# Function
def print_word(word_, multiplier_):
    for i in range(multiplier_):
        print(word_)


# Main Routine
word = input("Word to print: ")
multiplier = int(input("How many times: "))
print_word(word, multiplier)
