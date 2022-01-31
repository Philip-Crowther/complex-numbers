#!/usr/bin/env python

class ComplexNumber:
    """representation of a complex number"""
    def __init__(self, real_part=0, imaginary_part=0):
        self.real = real_part
        self.imaginary = imaginary_part

    @classmethod
    def from_str(cls, str):
        """class constructor from a string"""
        pass

    @classmethod
    def from_angle(cls, angle, magnitude):
        """constructs complex number from angle and magnitude"""
        pass


    @property
    def angle(self):
        pass

    @property
    def magnitude(self):
        """returns the magnitude of complex number"""
        return (self.real ** 2 + self.imaginary ** 2) ** 1/2

    def __repr__(self):
        """returns a representation of the complex number"""
        operator = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {operator} {abs(self.imaginary)}"

    def __str__(self) -> str:
        """returns a string representation of a comlex number"""
        operator = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {operator} {abs(self.imaginary)}i"

    def __add__(self, addend):
        """implementation of complex addition"""
        pass

    def __sub__(self, subtrahend):
        """implementation of complex subtraction"""
        pass

    def __mul__(self, factor):
        """implementation of complex multiplication 
        (scale by magnitude and add angles)"""
        new_magnitude = self.magnitude * factor.magnitude
        new_angel = self.angle + factor.angle
        return ComplexNumber.from_angle(new_angel, new_magnitude)

    def __truediv__(self, divisor):
        """Implementation of complex division
        (shrink by magnitude and subtract angles)"""
        pass

    def __abs__(self):
        """return absolute value of the complex number"""
        return self.magnitude

    

if __name__ == "__main__":
    main()

