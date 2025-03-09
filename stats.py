def count_words(text):
    text = text.split()
    return len(text)

def count_char(chars):
    chars = chars.lower()
    char_count = {}
    for i in chars:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] +=1
    return char_count

#print(count_char("123456789"))

def sorted_chars(unsorted):
    #alpha_only = unsorted.isalpha()
    list_of_dicts = [{"char": char, "count": count} 
                     for char, count in unsorted.items() if char.isalpha()]
    list_of_dicts.sort(reverse=True, key=lambda x: x["count"])
    return list_of_dicts

