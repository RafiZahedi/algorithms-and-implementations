def find_smallest_integer(num):
    if num == 0:
        return 10  # Special case: 0 can't be represented as a product of digits

    digits = []
    # Find the digits that make up the given number
    for i in range(9, 1, -1):
        while num % i == 0:
            digits.append(i)
            num //= i

    # If the number couldn't be completely factorized into digits
    if num > 1:
        return -1

    # Build the smallest integer using the found digits
    result = 0
    while digits:
        result = result * 10 + digits.pop()

    return result

# Test the function
num = int(input())
smallest_integer = find_smallest_integer(num)
print(smallest_integer)
