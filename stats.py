def get_book_text(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    book_strings = get_book_text(book)
    words = len(book_strings.split())

    print(f"{words} words found in the document")

(word_count("books/frankenstein.txt"))

def char_count(book):
    dict = {}
    characters = get_book_text(book)
    lcase_char = characters.lower()
    for char in lcase_char:
        if char not in dict:
            dict.update({char: 1})
        else:
            dict[char] += 1
    return dict

char_count("books/frankenstein.txt")