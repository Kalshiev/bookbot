def count_words(book_contents):
    words = book_contents.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_chars(book_contents):
    words = book_contents.split()
    chars = {}
    for word in words:
        for char in word:
            low_char = char.lower()
            if low_char not in chars:
                chars[low_char] = 1
            else:
                chars[low_char] += 1
    return chars

def sort_on(items):
    return items["num"]

def chars_report(char_dict):
    char_list = []
    char_keys = char_dict.keys()
    for c in char_keys:
        dictionary = dict(char = c, num = char_dict[c])
        char_list.append(dictionary)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

