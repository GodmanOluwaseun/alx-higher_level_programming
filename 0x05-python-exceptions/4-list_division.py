#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list =  []
    try:
        for i in range(list_length):
            is_int_float_1 = isinstance(my_list_1[i], (int, float))
            is_int_float_2 = isinstance(my_list_2[i], (int, float))
            if is_int_float_1 and is_int_float_2:
                div = my_list_1[i] / my_list_2[i]
                new_list.append(div)
    except ZeroDivisionError:
        new_list.append(0)
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
