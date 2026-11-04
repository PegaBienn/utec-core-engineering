#!/usr/bin/env python3
"""Módulo para escribir contenido en archivos de texto."""


def write_file(filename="", text=""):
    """ archivo UTF-8 y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as archivo:
        return archivo.write(text)
