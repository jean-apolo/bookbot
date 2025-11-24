import sys
from stats import get_word_count, get_char_count, get_sorted_char_count

def get_book_text(book_path):
    with open(book_path) as book:
        book_text = book.read()
    return book_text

def main():
    # Process arguments
    args = sys.argv
    if len(args) < 2 or len(args) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use second arg that will contain the path
    book_to_process = sys.argv[1]

    book_text_string = get_book_text(book_to_process)
    num_words = get_word_count(book_text_string)
    char_count_list = get_char_count(book_text_string)
    sorted_char_count_list = get_sorted_char_count(char_count_list)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_to_process}...')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for char_count in sorted_char_count_list:
        if char_count["char"].isalpha():
            print(f'{char_count["char"]}: {char_count["num"]}')
    print("============= END ===============")

if __name__=="__main__":
    main()
