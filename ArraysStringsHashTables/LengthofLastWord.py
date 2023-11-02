
def length_of_last_word(s):
    word = s.split()[-1]
    return len(word)


if __name__ == '__main__':
    print(length_of_last_word("luffy is still joyboy"))