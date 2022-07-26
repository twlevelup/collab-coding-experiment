
def is_valid_word_length(string):
    if not string.isdigit():
        return False
    if int(string) not in range(4,12):
        return False
    return True
