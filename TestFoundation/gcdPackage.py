'''
This file is demonstrate of greatest common factor in the mathematics computationally
*** Theory of the greatest common factor in computer science theory ***
If A = 0 , so GCD(A,B) = B. If, B = 0; This will be vice versa
Let say: A is a quotient equation (A = B*y + R); Then GCD(A,B) = GCD(B,R)
** Using Recursive Method **

'''

class gcds:
    def __init__(self):
        pass
    
    def gcdTwoArgs(self,a:int , b:int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            remainder = a % b
            return self.gcdTwoArgs(b,remainder)
    
    def gcdThreeArgs(self,a:int , b:int , c:int) -> int:
        if c == 0:
            self.gcdTwoArgs(a,b)
        else:
            remainders = self.gcdTwoArgs(a,b) % c
            return self.gcdTwoArgs(c,remainders)
    