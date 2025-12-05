import sys
from stats import count_words_in_text
from stats import count_characters_in_text
from stats import dictionary_to_sorted_list

#function takes the path to a .txt file
#and returns a string containing all of the text
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()



def main():
    #call get_book_text and print it out
    if not(len(sys.argv) == 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_text = sys.argv[1]
    text = get_book_text(path_to_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path_to_text + "...")
    print("----------- Word Count ----------")
    print(f"Found {count_words_in_text(text)} total words")
    print("--------- Character Count -------")
    letter_count = count_characters_in_text(text)
    list_of_dict = dictionary_to_sorted_list(letter_count)
    for dict in list_of_dict:
        if dict["char"].isalpha():
            print(dict["char"], end="")
            print(": ", end="")
            print(dict["num"], end="")
            print("\n")
        else:
            continue
    print("============= END ===============")
main()