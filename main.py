def get_book_text(filepath):
    file_contents = str()
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    print(file_contents)

main()
