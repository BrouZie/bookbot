def get_num_words(text):
    words_list = text.split()
    count = 0
    for word in words_list:
        count += 1
    return count


def get_num_characters(text):
    lowered_text = text.lower()
    character_counts = {}

    for char in lowered_text:
        character_counts[char] = character_counts.get(char, 0) + 1
    
    return character_counts

def sort_on(d):
    return d["num"]

def sort_dict_to_list(d):
    dict_list = []
    
    for key, value in d.items():
        if key.isalpha():
            dict_list.append({"char": key, "num": value})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_results(sorted_list, words):
    print(f"""\
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
""")
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")
    
    
    
