num = "1 2 3 4 5 6"
level = "c c c l u b"
num = [int(i) for i in num.split()]
level = level.split()
level_order_num = list()
for index, item in enumerate(num):
	level_order_num.append((level[index], index, item))
level_order_num.sort(key=lambda x: (x[0], x[1]))
ans = list()
print(level_order_num)
while level_order_num:
    i = 0
    while i < len(level_order_num):
        # print(level_order_num)
        if ans and ans[-1][0] == level_order_num[i][0]:
            i += 1
        else:
            ans.append(level_order_num[i])
            level_order_num.remove(level_order_num[i])
            print(level_order_num)
            print(ans)
    level_order_num = level_order_num[::-1]
    if level_order_num:
        ans.append(level_order_num[0])
        level_order_num = level_order_num[1:]
print(ans)