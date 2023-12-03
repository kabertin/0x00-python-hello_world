#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx >= len(my_list):
        return
    else:
        print("{:d}".format(my_list[idx]))
