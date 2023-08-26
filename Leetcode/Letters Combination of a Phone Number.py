letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
digits = '233'


def backtrack(index, str_builder):
    if len(str_builder) == len(digits):
        res.append("".join(str_builder))
        return

    for letter in letters[digits[index]]:
        str_builder.append(letter)
        backtrack(index + 1, str_builder)
        str_builder.pop()


res = []
backtrack(0, [])
print(res)
