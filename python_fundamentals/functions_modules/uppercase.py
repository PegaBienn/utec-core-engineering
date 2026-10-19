#!/usr/bin/env python3

def uppercase():
    palabra = input("Ingrese una palabra: ")
    resultado = ""
    
    for caracter in palabra:
        codigo_ascii = ord(caracter)
        if 97 <= codigo_ascii <= 122:
            resultado += chr(codigo_ascii - 32)
        else:
            resultado += caracter
            
    return resultado


print(uppercase())

