def get_num_words(text):
    words = text.split()  # 直接 split
    return len(words)


def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_on(item):
    return item["num"]

def sort_char_dict(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char.lower(), "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
