#!/usr/bin/env python3
"""módulo"""
def append_write(filename="", text=""):
    """agrega texto especifioc al final del contenido"""
    with open(filename, "a", encoding="utf-8") as archivo:
        return archivo.write(text)

