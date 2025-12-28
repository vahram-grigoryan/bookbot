def get_book_text(filepath):
    words = 0
    with open(filepath) as f:
        content = f.read()
        words = content.split()
    return len(words)

def get_char_frequency(filepath):
    char_frequency = {}

    with open(filepath) as f:
        content = f.read()
        for symbol in content:
            standard_symbol = symbol.lower()
            if standard_symbol in char_frequency:
                char_frequency[standard_symbol] += 1
            else:
                char_frequency[standard_symbol] = 1
    return char_frequency

def get_sorted_char_dicts(char_frequency):
    char_dict_list = []
    for char in char_frequency:
        if not char.isalpha():
            continue
        char_dict_list.append(
            {
                "char": char,
                "num": char_frequency[char],
            }
        )
    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list
    
def sort_on(item):
    return item["num"]