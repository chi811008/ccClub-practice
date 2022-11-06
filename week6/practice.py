M, N = [int(i) for i in input().split()]
O, P = [int(i) for i in input().split()]

data = list()
# [] [1, 2, 4, 5]
for i in range(M):
    data.extend([int(j) for j in input().split()]) # [1, 2, 4, 5]
print(data)

k = 0
for i in range(O):
    tmp = list()
    for j in range(P):
        tmp.append(data[k])
        k += 1
    print(" ".join(tmp))