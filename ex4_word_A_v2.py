""" Word starts with A
Created by Joseph Wong
14/02/2022
"""


# Check if word starts with A
def starts_with_a(word_to_check):
    if word[0] == "a" or "A":
        return True
    else:
        return False


# Main Routine
word = str(input("Enter word: "))
print(starts_with_a(word))
