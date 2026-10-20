#!/usr/bin/env python3
def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)

    resultado = 1
    for v in range(b):
        resultado *= a
        
    return resultado

