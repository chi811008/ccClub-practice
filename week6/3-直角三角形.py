# c = int(input())
# y, z = [int(i) for i in input().split()]
# if y > z:
#     y, z = z, y
# res = ["False"]
# for a in range(y, z + 1):
#     b = y
#     while b < z + 1:
#         if (a ** 2 + b ** 2 == c ** 2):
#             res[0] = "True"
#             break
#         b += 1
# print(res[0])

c = int(input())
y, z = [int(i) for i in input().split()]
if y > z:
    y, z = z, y
res = ["False"]
c_square = c ** 2
for a in range(y, z + 1):
    a_square = a ** 2
    head = y
    tail = z
    while head <= tail:
        mid = (head + tail) // 2
        if (a_square + mid ** 2 == c_square):
            res[0] = "True"
            break
        elif (a_square + (mid ** 2)) < c_square:
            head = mid + 1
        else:
            tail = mid - 1
print(res[0])