"""Proporciona una clase base para figuras geométricas."""


class BaseGeometry:
    """Define una interfaz de área y una validación común para las figuras."""

    def area(self):
        """Lanza una excepción hasta que una subclase implemente el cálculo."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que el valor de un parámetro sea un entero positivo."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
