#!/usr/bin/env python

class ComplexNumber:
    """representation of a complex number"""
    def __init__(self, real_part=0, imaginary_part=0):
        self.real = real_part
        self.imaginary = imaginary_part

    @property
    def angle(self):
        pass

    @property
    def magnitude(self):
        pass

    def __repr__(self):
        return f"ComplexNumber(real='{self.real}', imaginary={self.imaginary})"

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, addend):
        pass

    def __sub__(self, subtrahend):
        pass

    def __mul__(self, factor):
        new_magnitude = self.magnitude * factor.magnitude
        new_angel = self.angle + factor.angle
        return ComplexNumber.from_angle(new_angel, new_magnitude)

    def __truediv__(self, divisor):
        pass

    def __abs__(self):
        pass

    

if __name__ == "__main__":
    main()

