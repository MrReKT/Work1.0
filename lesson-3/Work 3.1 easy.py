__author__ = "Барыбин, Вячеслав, Русланович"

Fruits = ['Apple', 'Banana', 'Kivi', 'Watermelon']
last_name = len(Fruits)
for i in range(last_name):
    print(str(i + 1) + '.' + '{}'.format(Fruits[i]))