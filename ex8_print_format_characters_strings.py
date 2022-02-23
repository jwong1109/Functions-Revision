""" Print and format specified characters from a string
Created by Joseph Wong
15/02/2022
"""


# Function
def format_word(word_, num_letters_):
    part1 = word_[0:num_letters_].upper()
    part2 = word_[num_letters_:]
    print(f"{part1}{part2}")


# Main Routine
word = input("Word to print: ")
num_letters = int(input("Number of letters: "))
format_word(word, num_letters)
