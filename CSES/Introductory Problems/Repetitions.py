dna = input()

max_len = 1
last_char = dna[0]
cur_len = 1
for char in dna[1:]:
    if char == last_char:
        cur_len += 1
        max_len = max(max_len, cur_len)
        continue
    else:
        last_char = char
        cur_len = 1
print(max_len)
