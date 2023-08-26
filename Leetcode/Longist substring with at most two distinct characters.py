def length_of_longest_substring_two_distinct(s):
    # Initialize variables
    left, right = 0, 0
    max_length = 0
    char_count = {}

    # Iterate through the string
    while right < len(s):
        # Add the character at 'right' to the char_count dictionary
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink the window until only two distinct characters are present
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update the max_length
        max_length = max(max_length, right - left + 1)

        right += 1

    return max_length


# Test the function
s = "eceba"
print(length_of_longest_substring_two_distinct(s))  # Output: 3 (the longest substring is "ece")
