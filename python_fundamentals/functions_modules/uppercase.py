#!/usr/bin/env python3


def uppercase(str):
    for caracter in str:
        if 97 <= ord(caracter) <= 122:
            caracter = chr(ord(caracter) - 32)
        print("{}".format(caracter), end="")
    print("")

