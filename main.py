from stats import word_count, char_count

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def main():
    print (get_book_text("books/frankenstein.txt"))

main()   

book_characters = char_count("books/frankenstein.txt")
print(book_characters)