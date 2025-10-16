def count_words(text):
    word_count = len(text.split())
    return word_count

def character_counter(text):
    character_dict = {}
    for letter in text.lower():
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict


def sort_on(items):
    return items["num"]

def clean_result(counts):
    result = []
    for ch, num in counts.items():
        result.append({"char": ch,
                     "num": num})
    result.sort(key=sort_on, reverse = True)
    return result

