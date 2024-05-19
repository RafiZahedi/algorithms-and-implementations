def solve():
    # def is_subsequence_present(binary_string, subsequence):
    #     if len(binary_string) < len(subsequence):
    #         return False
    #
    #     subsequence_length = len(subsequence)
    #     subsequence_index = 0
    #
    #     for char in binary_string:
    #         if char == subsequence[subsequence_index]:
    #             subsequence_index += 1
    #             if subsequence_index == subsequence_length:
    #                 return True
    #
    #     return False

    def max_subsequence(string_1, string_2, len_a, len_b):
        i = 0
        count = 0
        for char in string_2:
            if i < len_a and string_1[i] == char:
                i += 1
                count = max(count, i)
        return count

    n, m = map(int, input().split())
    str_1 = input()
    str_2 = input()
    return max_subsequence(str_1, str_2, n, m)


for _ in range(int(input())):
    print(solve())
