
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} found in the document")
    print(get_character_count(text))

def get_character_count(text):
    lower_case = text.lower()
    char_count = {}

    for char in lower_case:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return char_count
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()