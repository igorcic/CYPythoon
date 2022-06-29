from math import sqrt

class Triangulo:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    
    def Area(self):
        p = (self.A + self.B + self.C)/2
        area = sqrt(p * (p - self.A) * (p - self.B) * (p - self.C))
        return area