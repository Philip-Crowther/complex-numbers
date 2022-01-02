#!/usr/bin/env python

class ComplexNumber:
    """representation of a complex number"""
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __repr__(self):
        return f"ComplexNumber(real='{self.real}', imaginary={self.imaginary})"

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"
    


if __name__ == "__main__":
    main()

