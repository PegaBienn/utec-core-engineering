#!/usr/bin/env python3
"""Añade una representación de texto para los cuadrados."""

BaseSquare = __import__("1-square").Square


class Square(BaseSquare):
    """Cuadrado con una descripción que identifica su figura."""

    def __str__(self):
        """Devuelve la descripción del cuadrado con sus dimensiones."""
        return super().__str__().replace("[Rectangle]", "[Square]", 1)
