M, N = [int(i) for i in input().split()]
O, P = [int(i) for i in input().split()]
elements = list()
for i in range(M):
    elements.extend([int(i) for i in input().split()])

k = 0
for j in range(O):
    res = list()
    for n in range(P):
        res.append(str(elements[k]))
        k += 1
    print(" ".join(res))