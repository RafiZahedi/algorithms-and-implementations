s = "PAYPALISHIRING"
numRows = 3
matrix = [[] for _ in range(numRows)]
index = 0
step = -1
for char in s:
    matrix[index].append(char)
    if index == 0:
        step = 1
    elif index == numRows - 1:
        step = -1
    index += step
for i in range(numRows):
    matrix[i] = ''.join(matrix[i])
print(''.join(matrix))
