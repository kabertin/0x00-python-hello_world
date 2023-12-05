#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        comp = my_list[0]
        from num in my_list:
            if num >= comp:
                comp = num
    return comp
