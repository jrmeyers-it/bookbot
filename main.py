from stats import total_word_count, report_book_letter_count
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_uri = sys.argv[1]
        print("=============== BOOKBOT ===============")
        print(f"Analyzing book found at {book_uri}")
        print("------------- Word Count --------------")
        total_words = get_book_text(book_uri)
        print(f"Found {len(total_words.split())} total words")
        print("----------- Character Count -----------")
        letter_count_list = report_book_letter_count(get_book_text(book_uri))
        for letter_count in letter_count_list:
            print(f"{letter_count["char"]}: {letter_count["num"]}")
            print("")
        print("================= END =================")
main()