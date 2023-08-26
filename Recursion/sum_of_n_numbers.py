n = 10


# Also the Formula is n(n + 1) / 2

def sum_of_n_numbers(n):
    if n == 1:
        return n
    return n + sum_of_n_numbers(n - 1)


print(sum_of_n_numbers(n)) 
print((n * (n + 1) / 2))