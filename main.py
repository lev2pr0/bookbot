# Import from stats.py
from stats import get_word_count,get_char_count,sort_char

# Function to return book content
def get_book_text(filepath):
    file_contents = str()
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"

    # Get book content
    file_contents = get_book_text(filepath)

    # Get word & character count with sorting results
    num_words = get_word_count(file_contents)
    num_char = get_char_count(file_contents)
    results = sort_char(num_char)

    # Print report with excluding non-alphabetic characters from count
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for count in results:
        if str.isalpha(count["char"]) == True:
            print(f"{count["char"]}: {count["num"]}")
        else:
            pass

main()
