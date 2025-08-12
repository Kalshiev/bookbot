from stats import count_words, count_chars, chars_report
import sys

n = len(sys.argv)

if n < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def main():
    directory = sys.argv[1]
    text = get_book_text(directory)
    word_count = count_words(text)
    char_dict = count_chars(text)
    char_stats = chars_report(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {directory}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_stats:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()
