# in this problem if we find the relationship between left shift and right shift
# we can simply convert each right shift to left shift
# just by making the amount negative we can perform only left_shift and it will be same as right shift
# if n == 8 and we need to do a 7 right shift, 7 right shifts is equal to 1 left shift
# so we just make the right shift negative which is -7, and now n - 7 is 1 so we saw that right shift is 1 left shift
def left_shift_string(input_str, num_shifts):
    num_shifts %= len(input_str)
    return input_str[num_shifts:] + input_str[:num_shifts]


s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
left_amount = 0
for direction, amount in shift:
    if direction == 1:
        amount = - amount
    left_amount += amount

print(left_shift_string(s, left_amount))
