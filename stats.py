# Function counts the number of words in a text
# The input argument is a path to the text, which is then
# opened and turned to string 
def count_words_in_text(input_text):
    words = input_text.split()
    return len(words)

# Function creates a dictionary that stores the characters 
# and how many times they have apperaed in the input text
# Input is a string
def count_characters_in_text(input_text):
    letter_count = {}
    input_lower_case = input_text.lower()
    for charact in input_lower_case:
        # if the letter is already in the dict. add one to
        # existing value
        if charact in letter_count:
            letter_count[charact] = letter_count[charact] + 1
        else:
            # if the letter isn't inside of the dict.
            # add the letter and set it's count to 1
            letter_count[charact] = 1
    return letter_count

# Helper function to return 
def num_of_charact_in_dict(char_dictionary):
    return char_dictionary["num"]

# A function to take our dictionary and turn it into
# a sorted list, this list will then be used to write a 
# neat report about the book
def dictionary_to_sorted_list(dictionary_of_characters):
    list_of_dictionaries = []
    for letter in dictionary_of_characters:
        list_of_dictionaries.append({"char": letter,
                                     "num": dictionary_of_characters[letter]})
    list_of_dictionaries.sort(key=num_of_charact_in_dict, reverse=True)
    return list_of_dictionaries