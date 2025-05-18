from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    character_count = get_num_characters(text)
    sorted_list = sort_dict_to_list(character_count)
    print_results(sorted_list, num_words)



def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content




main()