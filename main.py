import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = sys.argv[1]
    #print(get_book_text(path_to_file))

main()

from stats import count_words

book_text = get_book_text(sys.argv[1])
word_count = count_words(book_text)
#print(f"{word_count} words found in the document")

from stats import count_char

char_count = count_char(book_text)
#print(char_count)

from stats import sorted_chars

chars_sort = sorted_chars(char_count)
#print(chars_sort)

print("============ BOOKBOT ==========")
print(f"Analyzing book found at {sys.argv[1]}...")
print("--------- Word Count ---------")
print(f"Found {word_count} total words")
print("------- Character count -------")
for item in chars_sort:
    print(f"{item['char']}: {item['count']}")
print("============ END ===============")