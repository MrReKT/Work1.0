one_list = ["Яблоко", "Ананас" "Дыня", "Банан", "Черешня", "Киви"]
Two_list = ["Клубника", "Банан", "Яблоко","Киви", "Абрикос"]
three_list = [fruit for fruit in one_list if fruit in Two_list]
print(three_list)
