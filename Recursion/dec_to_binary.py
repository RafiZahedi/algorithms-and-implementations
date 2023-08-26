number = 10
result = ''


def dec_to_bin(number, result):
    if number == 0:
        return result
    result = str(number % 2) + result
    return dec_to_bin(number // 2, result)

print(dec_to_bin(number, result))