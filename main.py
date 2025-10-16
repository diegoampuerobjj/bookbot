from stats import count_words, character_counter, clean_result
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(book):
    with open(book) as f:
        read_contents = f.read()
        return read_contents


def main():
    book_text = get_book_text(book_path)
    counted_words = count_words(book_text)
    character_count = character_counter(book_text)
    sorted_result = clean_result(character_count)
      
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {counted_words} total words\n--------- Character Count -------")
    
    for item in sorted_result:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")



main()

