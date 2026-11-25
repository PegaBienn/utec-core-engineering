#!/usr/bin/env python3
"""Representa rectángulos con dimensiones enteras positivas."""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectángulo definido por su ancho y su altura."""

    def __init__(self, width, height):
        """Valida y guarda las dimensiones del rectángulo."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
