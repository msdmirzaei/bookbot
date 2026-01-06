def number_of_words(text):
    return len(text.split())


def char_count(text):
    res = {}
    for ch in text:
        ch = ch.lower()
        if ch in res:
            res[ch]["num"] += 1
        else:
            res[ch] = {
                "char": ch,
                "num": 1,
            }
    return list(res.values())
        

def sort_on(items):
    return items["num"]

def sort_char_counts(char_counts):
    char_counts.sort(reverse=True, key=sort_on)
    return char_counts