
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    list_char_count = [{"character": char, "num": count} for char, count in character_count.items()]
    list_char_count.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in list_char_count:
        print(f"The '{item['character']}' character was found {item['num']} times")
    print("--- End report ---")
    

def sort_on(item):
    return item["num"]

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