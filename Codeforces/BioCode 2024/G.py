MOD = 10 ** 9 + 7


def digit_sum(x):                 """Calculate the sum of digits of x.

                                  return sum(int(d) for d in str(x))

def count_valid_numbers(l, r, k):

                                  """


Count
numbers
n in the
range[10 ^ 1, 10 ^ r) that
satisfy
the
condition
D(k
W
start = 10 ** 1

end = 10 ** r

count = 0

for n in range(start, end):  if
digit_sum(k * n) == k
digit_sum(n): \

count = (count + 1) % MOD

return count

# Reading input

t = int(input())

results = []

for in range(t):
    l, r, k = map(int, input().split())
    result = count_valid_numbers(l, r, k)

    results.append(result)

# Output results

for result in results:            print(result)
