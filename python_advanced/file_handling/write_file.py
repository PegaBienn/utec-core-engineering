#!/usr/bin/env python3
"""modulo"""
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as archivo:
        archivo.write(text)
        return archivo.write(text)
