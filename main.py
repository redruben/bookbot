import sys
from stats import word_count, char_count, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def main():
    print(get_book_text(book))

book_characters = char_count(book)

sorted = sort_chars(book_characters)

def report(char_count):
    for s in char_count:
        if s["char"].isalpha():
            print(f"{s["char"]}: {s["num"]}")
    
def styling(book):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book} \n----------- Word Count ----------")
    word_count(book)
    print("--------- Character Count -------")
    report(sorted)

styling(book)
