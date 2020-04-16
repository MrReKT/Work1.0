__author__ = "Барыбин, Вячеслав, Русланович"

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = []
c = len(a)
for i in range(c):
    if a[i] % 2 == 0:
        b.append(a[i] / 4)
else:
        b.append(a[i] * 2)
print(b)
