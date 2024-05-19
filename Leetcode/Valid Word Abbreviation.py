def validWordAbbreviation(word: str, abbr: str) -> bool:
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if word[i] == abbr[j]:
            i += 1
            j += 1
            continue

        if abbr[j] <= '0' or abbr[j] > '9':
            return False
        # store the starting point of 'j', because it's the starting point of the digits
        start = j
        while j < len(abbr) and '0' <= abbr[j] <= '9':  # while 'j' is a digit, expand
            j += 1
        num = int(abbr[start:j])  # from the start till 'j' are the digits
        i += num  # now move the 'i' cells ahead

    # at the end both 'i' and 'j' must be at the end of the strings
    return i == len(word) and j == len(abbr)


print(validWordAbbreviation("internationalization", "i12iz4n"))  # Output: True
print(validWordAbbreviation("apple", "a2e"))  # Output: False
print(validWordAbbreviation("aaaaaa", "a4a"))  # Output: True
