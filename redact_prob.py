
def redact(words, banned_words):
    new_arr = []

    banned_set = set(banned_words)

    for item in words:
        if item not in banned_words:
            new_arr.append(item)

    return new_arr
