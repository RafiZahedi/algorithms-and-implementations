Input = input()


def is_palindrome(Input):
    if len(Input) == 0 or len(Input) == 1:
        return True
    if Input[0] == Input[len(Input) - 1]:
        return is_palindrome(Input[1:len(Input) - 1:])
    return False


print(is_palindrome(Input))
