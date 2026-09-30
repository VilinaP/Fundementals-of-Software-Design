def dcg(numerator: int, denominator: int):
    while denominator != 0:
        numerator, denominator = denominator, numerator%denominator
    return numerator

class Fraction:
    def __init__(self, numerator: int, denominator: int = 1): # TODO: make denominator optional!
        self.numerator = numerator
        self.denominator = denominator
        simplify = dcg(self.numerator, self.denominator)
        if simplify != 0:
            self.numerator = self.numerator//simplify
            self.denominator = self.denominator//simplify

    def __str__(self):
        ''' Gives the human representation of the string 
        >>> print(Fraction(10, 2))
        Fraction(5)
        >>> print(Fraction(2, 3))
        Fraction(2, 3)
        >>> print(Fraction(5, 35))
        Fraction(1, 7)
        '''
        return f"Fraction({self.numerator}" + (f', {self.denominator})' if self.denominator != 1 else ')')
    def __repr__(self):
        ''' Gives a python representation of the class
        >>> Fraction(10, 2)
        Fraction(5)
        >>> Fraction(2, 3)
        Fraction(2, 3)
        >>> Fraction(5, 35)
        Fraction(1, 7)
        '''
        return f"Fraction({self.numerator}" + (f', {self.denominator})' if self.denominator != 1 else ')')
    def __eq__(self, other):
        ''' returns true is the fraction are the same, returns false is fractions are different
        >>> Fraction(10, 2) == Fraction(10, 2)
        True
        >>> Fraction(2, 3) == Fraction(2, 4)
        False
        >>> Fraction(5, 35) == Fraction(1, 7)
        True
        '''
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False
    def __lt__(self, other):
        ''' compares if one fractions is less then another
        >>> Fraction(10, 2) < Fraction(10, 2)
        False
        >>> Fraction(2, 3) < Fraction(2, 4)
        False
        >>> Fraction(5, 35) < Fraction(1, 7)
        False
        >>> Fraction(2, 4) < Fraction(2, 3)
        True
        '''
        if self.numerator * other.denominator < other.numerator * self.denominator:
            return True
        return False
    def __le__(self, other):
        ''' compares if one fractions is less then or equal to another
        >>> Fraction(10, 2) <= Fraction(10, 2)
        True
        >>> Fraction(2, 3) <= Fraction(2, 4)
        False
        >>> Fraction(5, 35) <= Fraction(1, 7)
        True
        >>> Fraction(2, 4) <= Fraction(2, 3)
        True
        '''
        if self == other or self < other:
            return True
        return False
    def __ne__(self, other):
        ''' compares if fractions are not equal to each other
        >>> Fraction(10, 2) != Fraction(10, 2)
        False
        >>> Fraction(2, 3) != Fraction(2, 4)
        True
        >>> Fraction(5, 35) != Fraction(1, 7)
        False
        >>> Fraction(2, 4) != Fraction(2, 3)
        True
        '''
        if self == other:
            return False
        return True
    def __gt__(self, other):
        ''' compares if one fractions is grater then another
        >>> Fraction(10, 2) > Fraction(10, 2)
        False
        >>> Fraction(2, 3) > Fraction(2, 4)
        True
        >>> Fraction(5, 35) > Fraction(1, 7)
        False
        >>> Fraction(2, 4) > Fraction(2, 3)
        False
        '''
        if self <= other:
            return False
        return True
    def __ge__(self, other):
        ''' compares if one fractions is grater then or equal another
        >>> Fraction(10, 2) >= Fraction(10, 2)
        True
        >>> Fraction(2, 3) >= Fraction(2, 4)
        True
        >>> Fraction(5, 35) >= Fraction(1, 7)
        True
        >>> Fraction(2, 4) >= Fraction(2, 3)
        False
        '''
        if self < other:
            return False
        return True

    def __add__(self, other):  
        ''' adds two fractions together
        >>> Fraction(10, 2) + Fraction(10, 2)
        Fraction(10)
        >>> Fraction(2, 3) + Fraction(2, 4)
        Fraction(7, 6)
        >>> Fraction(5, 35) + Fraction(1, 7)
        Fraction(2, 7)
        >>> Fraction(2, 4) + Fraction(2, 3)
        Fraction(7, 6)
        '''
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator*other.denominator)

    def __sub__(self, other):
        ''' subtracted one fraction from another
        >>> Fraction(10, 2) - Fraction(10, 2)
        Fraction(0)
        >>> Fraction(2, 3) - Fraction(2, 4)
        Fraction(1, 6)
        >>> Fraction(5, 35) - Fraction(1, 7)
        Fraction(0)
        >>> Fraction(2) - Fraction(2, 3)
        Fraction(4, 3)
        '''
        return Fraction((self.numerator*other.denominator - other.numerator*self.denominator), (self.denominator*other.denominator))

    def __mul__(self, other):
        ''' multiply one fraction by another
        >>> Fraction(10, 2) * Fraction(10, 2)
        Fraction(25)
        >>> Fraction(2, 3) * Fraction(2, 4)
        Fraction(1, 3)
        >>> Fraction(5, 35) * Fraction(1, 7)
        Fraction(1, 49)
        >>> Fraction(2) * Fraction(2, 3)
        Fraction(4, 3)
        '''
        return Fraction(((self.numerator) * (other.numerator)), (self.denominator*other.denominator))

    def __truediv__(self, other):
        ''' divide one fraction by another
        >>> Fraction(10, 2) / Fraction(10, 2)
        Fraction(1)
        >>> Fraction(2, 3) * Fraction(2, 4)
        Fraction(4, 3)
        >>> Fraction(5, 35) * Fraction(1, 7)
        Fraction(1)
        >>> Fraction(2) * Fraction(2, 3)
        Fraction(3)
        '''
        other = Fraction(other.denominator, other.numerator)
        return self*other
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()