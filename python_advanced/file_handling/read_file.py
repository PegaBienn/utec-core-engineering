#!/usr/bin/env python3
"""Módulo que puede leer e imprimir archivos.txt"""
def read_file(filename = ""):
    """Lee el archivo y lo imprime en stdout"""
    with open(filename, encoding="utf-8") as archivo:
        print(archivo.read(), end="")
