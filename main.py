import sys
from stats import count_words
from stats import character_count
from stats import sort_characters

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_contents = get_book_text(book)
    num_words = count_words(book_contents)
    num_characters = character_count(book_contents)
    sorted_book_list = sort_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") 
    for char_dict in sorted_book_list:
       char = char_dict["char"]
       count =char_dict["count"]
       if char.isalpha():
          print(f"{char}: {count}")
    print("============= END ===============")      

    


main()


    
    

