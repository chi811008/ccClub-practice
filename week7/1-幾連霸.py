s = "1"
ls = [int(i) for i in s.split()]
max_length = length = 1

for i in range(len(ls) - 1):
    if ls[i] + 1 == ls[i + 1]:
        length += 1
    else:
        length = 1
    max_length = max(max_length, length)
print(max_length)