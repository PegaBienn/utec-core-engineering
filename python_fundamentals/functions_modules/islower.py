#!/usr/bin/env python3
letra=input("ingrese algo: ")
def islower(letra):
    if  len(letra) != 1 or not (97 <= ord(letra) <= 127):
     print(False)
    else:
        print(True)

islower(letra)

