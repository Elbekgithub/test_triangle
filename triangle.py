class Triangle:
    """
    Simple Triangle class
    Inputs are for three sides of triangle
    """
    def __init__(self, a, b, c):
        if any((a <= 0, b <= 0, c <= 0)):
            raise ValueError("Negative input")
        if any((a + b <= c, a + c <= b, b + c <= a)):
            raise ValueError("Given inputs can not be triangle")
        self.a = a
        self.b = b
        self.c = c

    def get_triangle_type(self):
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isosceles"
        else:
            return "Scalene"
