def solve(source, target):
    most_left_char, minimum = 0, 1

    for c in target:

        # Get leftmost char after previously matched index
        most_left_char = source.find(c, most_left_char)

        # If not found
        if most_left_char == -1:

            # Get leftmost char from beginning of string and increase number of concatenated string
            most_left_char = source.find(c)
            minimum += 1

            # if not found, then target can't be formed. Return -1
            if most_left_char == -1:
                return most_left_char

        most_left_char += 1

    return minimum


source = 'abc'
target = 'abcbc'
print(solve(source,target))
