""" Longest Word
Created by Joseph Wong
17/02/2022
"""


# Function
def longest_word(string_list):
    longest = ""
    for i in string_list:
        if len(i) > len(longest):
            longest = i
    return longest


# Main Routine
print(longest_word(["Jack", "Tomato", "Cat"]))
print(longest_word(["Hi", "Dog", "Cat"]))

