import math

s = "PAYPALISHIRING"
n = len(s)
numRows = 3
numCols = math.ceil((n / (2 * numRows - 2)) * (numRows - 1))
matrix = [[' '] * numCols for _ in range(numRows)]

r, c = 0, 0
index_letter = 0

while index_letter < n:
    # down
    while r < numRows and index_letter < n:
        matrix[r][c] = s[index_letter]
        r += 1
        index_letter += 1
    r -= 2
    c += 1

    # up and right (Diagonal)
    while c < numCols and index_letter < n and r > 0:
        matrix[r][c] = s[index_letter]
        c += 1
        r -= 1
        index_letter += 1
res = ""
for row in matrix:
    res += "".join(row)
res = res.replace(" ", "")
print(res)