#!/usr/bin/env python3
"""Representa rectángulos con dimensiones enteras positivas."""

import base_geometry


class Rectangle(base_geometry.BaseGeometry):
    """Rectángulo definido por su ancho y su altura."""

    def __init__(self, width, height):
        """Valida y guarda las dimensiones del rectángulo."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
