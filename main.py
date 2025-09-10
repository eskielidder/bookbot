from stats import count_words, count_chars, create_letter_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        contents = (get_book_text(sys.argv[1]))
        num_words = count_words(contents)
        letter_dict = (count_chars(contents))
        letter_list = (create_letter_list(letter_dict))
        #print(letter_list)

        

        print("========== BOOKBOT ==========")
        print(f"Analyzing the book found at {sys.argv[1]}...")
        print("--------- Word Count --------")
        print(f"Found {num_words} total words")
        print("------ Character Count -------")
        for items in letter_list:
            #print(items)
            entry_list = []
            for item in items.values():
                entry_list.append(str(item))
                
            if entry_list[0].isalpha():
                print(f"{entry_list[0]}: {entry_list[1]}")
        print("============ END =============")


main()




