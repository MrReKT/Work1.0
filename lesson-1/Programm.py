__author__ = "Барыбин Вячеслав Русланович"

name = input("Введите Имя")
age = input("Введите Возраст")

diff = int(age) - 18
if diff == 0:
    print(name, "равен", age)
elif diff < 0:
    print(name, "Младше на", abs(diff), 'года(лет)')
else: 
    print(name, "Старше  на", diff, 'Года(нет)')
