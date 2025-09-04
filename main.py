
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main():
    book_path=sys.argv[1]
    with open(book_path) as f:
        text = get_book_text(f)
    num_words = get_num_words(text)
    char_count = get_letter_count(text)
    sorted_list = get_sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}..")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    #sorted_list.sort(reverse=True, key=sort_on)
    #print(sorted_list)
    print("============= END ===============")

def get_book_text(f):
    # f is a file object
    file_contents = f.read()
    return file_contents


from stats import get_num_words, get_letter_count, sort_on, get_sorted_list

main()