def count_words(book):
    return len(book.split())

def character_count(book):
    characters = {}
    for character in book.lower():
        if character in characters:
            characters[character] += 1 
        else:
             characters[character] = 1 
    return characters
            
def sort_characters(char_dict):
    char_list = []
    for char, count in char_dict.items():
       char_list.append({"char": char, "count": count}) 

    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list


    




