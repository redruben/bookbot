def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def main():
    print (get_book_text("books/frankenstein.txt"))

main()

def word_count(book):
    book_strings = get_book_text(book)
    words = len(book_strings.split())

    print(f"{words} words found in the document")

(word_count("books/frankenstein.txt"))

        