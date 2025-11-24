# This function takes text as a string and
# returns the number of words in the text
def get_word_count(book_text_string):
    return len(book_text_string.split())

# This function obtains the book text as a string 
# and returns the number of times each character appears
# (including symbols and spaces) in the form of a python
# dictionary where each key is associated with the unique
# character found and its value is the number of times 
# each character appears in the book text. Note that
# the result is not sorted and also includes non alphanumeric
# characters
def get_char_count(book_text_string):
    char_count = {}
    book_text_string_lowercase = book_text_string.lower()

    for letter in book_text_string_lowercase:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1

    return char_count

# This function takes a dictionary and returns the value of
# the "num" key. This is mainly used as a helper function
# for use in conjunction with the .sort method to tell it
# how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

# This function sorts a character count, as a dictionary
# (see get_char_count function) and sorts it by key pair.
# It will return the sorted character count as a dictionary.
# Note that it shall ingore non-alphanumeric characters
def get_sorted_char_count(unsorted_char_count):
    char_count_list = []

    # Generate a list of dictionaries.
    for character, count in unsorted_char_count.items():
        char_count_list.append({"char": character, "num": count})

    # Sort through the list of dictionaries using the .sort
    # method and the helper function to tell it to sort by the
    # character count
    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list
