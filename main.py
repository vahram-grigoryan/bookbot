import sys
from stats import get_book_text, get_char_frequency, get_sorted_char_dicts

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def main():
    num_words = get_book_text(filepath)
    char_freq = get_char_frequency(filepath)
    sorted_char_list = get_sorted_char_dicts(char_freq)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_list:
        print(f"{char_dict['char']}: {char_dict['num']}")

main()
