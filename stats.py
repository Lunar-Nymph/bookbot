def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    #print(new_string)
    #char_list = list(new_string)
    char_dict = {}
    for c in text:
        low = c.lower()
        if low in char_dict:
            char_dict[low] += 1
        else:
            char_dict[low] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_sorted_list(char_count):
    unsorted = char_count
    dict_list = []
    for key in unsorted:
        value = unsorted[key]
        dict_list.append({"char":key, "num":value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

    
