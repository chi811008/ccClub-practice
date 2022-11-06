n = int(input())
l = 0
r = n - 1
matrix = list()
for i in range(n):
    matrix.append(input().split(","))


print(matrix)

while l < r:
    for i in range(r - l):
        top, bottom = l, r

        # save the left top
        left_top = matrix[top][l]

        # move left
        matrix[top + i][l] = matrix[top + i + 1][l]

        # move bottom
        matrix[bottom][l + i] = matrix[bottom][l + i + 1]

        # move right
        matrix[r][bottom - i] = matrix[r][bottom - i - 1]

        # move top
        matrix[top][r - i] = matrix[top][r - i - 1]

        matrix[top][l + 1] = left_top
    l += 1
    r -= 1
print(matrix)