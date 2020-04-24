def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое" "Ввиденных чисел")

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as err:
    print("Ошибка:", err, "Введены не правильно числа. ")
except Exception as arr:
    print("Ошибка:", err)