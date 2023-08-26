import collections

s = "eceba"
k = 2
counter = collections.Counter()
max_size = 0
left = 0
for right in range(len(s)):
    counter[s[right]] += 1
    while len(counter) > k:
        counter[s[left]] -= 1
        if counter[s[left]] == 0:
            del counter[s[left]]
        left += 1
    max_size = max(max_size, right - left + 1)
print(max_size)

