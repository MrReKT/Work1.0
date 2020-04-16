n = int(input("Ведите числа:"))
list_one = []
for i in range(n):
    list_one.append(random.randint(-100, 100))
print(list_one)