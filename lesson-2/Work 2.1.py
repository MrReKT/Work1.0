# x__author__ = "Барыбин Вячеслав Русланович"

caption  = input("Четные или Нечетные: ")
a = 0

if caption == "Четные":
      a = 0
      while a < 20:
            print(a, end = '')
            a += 2
elif caption == "Нечетные":
      a = 1
      while a < 20:
            print(a, end = '')
            a += 2
else: 
      print("Я не понимаю, что вы вводите")