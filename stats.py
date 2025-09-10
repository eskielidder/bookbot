def count_words(contents):
    count = 0
    all_words = contents.split()
    for word in all_words:
        count += 1
    return count

def count_chars(contents):
    char_dict = {}
    
    contents = contents.lower()
    for letter in contents:
        if letter not in char_dict:
            char_dict[letter] = 1
        elif letter in char_dict:
            char_dict[letter] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def create_letter_list(letter_dict):
    letter_list = []
    char_dict = {}
    dict_items = letter_dict.items()
    for key, value in dict_items:
        char_dict = {"char":key,"num":value}
        letter_list.append(char_dict)
    letter_list.sort(reverse=True,key=sort_on)
    return letter_list


