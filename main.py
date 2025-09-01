import sys
from stats import sort_char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for char in text:
        lower = char.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

def print_report(word_count, sorted_chars, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_path = sys.argv[1]

    
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_char_dict(char_counts)
    print_report(word_count, sorted_chars, book_path)

main()
