

def my_var():
    my_int = int(42)
    print(f"{my_int} est de type {type(my_int)}")
    my_str = str("42")
    print(f"{my_str} est de type {type(my_str)}")
    my_str2 = "quarante-deux"
    print(f"{my_str2} est de type {type(my_str2)}")
    my_float = float(42)
    print(f"{my_float} est de type {type(my_float)}")
    my_bool = True
    print(f"{my_bool} est de type {type(my_bool)}")
    my_lst = [42]
    print(f"{my_lst} est de type {type(my_lst)}")
    my_dict = {42: 42}
    print(f"{my_dict} est de type {type(my_dict)}")
    my_tuple = (42, )
    print(f"{my_tuple} est de type {type(my_tuple)}")
    my_set = set()
    print(f"{my_set} est de type {type(my_set)}")


if __name__ == "__main__":
    my_var()
