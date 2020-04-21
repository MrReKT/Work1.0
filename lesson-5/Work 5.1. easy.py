def my_Function(a,b):
    return a**b 

if __name__ == "__main__":
    one_list = [1, 2, 4, 0]
    second_list = [my_Function(a, 2) for a in one_list]
    print(second_list)