from stats import word_count, char_count, sort_chars

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def main():
    print (get_book_text("books/frankenstein.txt"))

book_characters = char_count("books/frankenstein.txt")

sorted = sort_chars(book_characters)

def report(char_count):
    for s in char_count:
        if s["char"].isalpha():
            print(f"{s["char"]}: {s["num"]}")
    
def styling(book):
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    word_count(book)
    print("--------- Character Count -------")
    report(sorted)

styling("books/frankenstein.txt")
