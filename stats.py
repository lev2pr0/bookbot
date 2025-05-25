def get_word_count(text):
    word_list = str.split(text)
    return len(word_list)

def get_char_count(text):
    converted_char = str.lower(text)
    char_count = {}
    for char in converted_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char(char_count):

    def get_dict_list(char_count):
        dict_list = []
        dict_store = {}
        for char in char_count:
            num = char_count[char]
            dict_store = dict(char=char, num=num)
            dict_list.append(dict_store)
        return dict_list

    def sort_on(dict_list):
        return dict_list["num"]

    get_dict_list(char_count)
    sorted_list = sorted(get_dict_list(char_count), reverse=True, key=sort_on)
    return sorted_list
