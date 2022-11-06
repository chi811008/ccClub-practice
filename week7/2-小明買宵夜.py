s = "8 12 40 14"
meals = input().split()
ls = [int(i) for i in input().split()]
k = int(input())
residual = k
item = [0] * 2
len_ls = len(ls)
for i in range(len_ls):
    r = k - ls[i]
    for j in range(i, len_ls):
        if r - ls[j] >= 0 and (r - ls[j] < residual):
            residual = r - ls[j]
            item[0] = i
            item[1] = j
print(meals[item[0]] + " " + meals[item[1]])