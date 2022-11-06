# input -> string
test = "7414"
def apple_label(test):
    ans = list()
    for n in test:
        n = int(n)
        if n > 6:
            ans.append("True")
        else:
            ans.append("False")
    return " ".join(ans)
a = apple_label(test)
print(a)

b = " ".join(["True" if int(n) > 6 else "False" for n in test])
print(b)