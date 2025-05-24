from stats import get_word_count

def get_book_text(filepath):
    file_contents = str()
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    num_words = get_word_count(file_contents)
    print(f"{num_words} words found in the document")

main()
