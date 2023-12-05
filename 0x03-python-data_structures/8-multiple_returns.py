#!/usr/bin/python3
def multiple_returns(sentence):
    el_1 = len(sentence)
    tup = ()
    x = None
    if not sentence:
        tup = (el_1, x)
    else:
        tup = (el_1, sentence[0])
    return tup
