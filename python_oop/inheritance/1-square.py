#!/usr/bin/env python3
"""Representa cuadrados con lados de longitud entera positiva."""

Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Rectángulo con ancho y altura iguales."""

    def __init__(self, size):
        """Valida el lado e inicializa las dimensiones del rectángulo."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Devuelve el cuadrado de la longitud del lado."""
        return self.__size ** 2
