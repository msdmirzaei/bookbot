import sys
from stats import number_of_words, char_count, sort_char_counts


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    num_words = number_of_words(text)
    num_chars = char_count(text)
    sorted_char_counts = sort_char_counts(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch in sorted_char_counts:
        if ch["char"].isalpha():
            print(f"{ch["char"]}: {ch["num"]}")


main()






