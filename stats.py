import sys

book = sys.argv[1]

def get_book_text(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    book_strings = get_book_text(book)
    words = len(book_strings.split())

    print(f"Found {words} total words")

word_count(book)

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

def sort_help(list):
    return list["num"]

def sort_chars(dictionary):
    list = []
    for char, num in dictionary.items():
        list.append({"char": char,"num": num})
    list.sort(reverse=True, key=sort_help)
    return list
