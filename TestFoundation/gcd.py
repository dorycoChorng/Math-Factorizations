'''
This file is demonstrate of greatest common factor in the mathematics computationally
*** Theory of the greatest common factor in computer science theory ***
If A = 0 , so GCD(A,B) = B. If, B = 0; This will be vice versa
Let say: A is a quotient equation (A = B*y + R); Then GCD(A,B) = GCD(B,R)
** Using Recursive Method **

'''

import time

# When there is 2 arguements taken
def gcdTwoArgs(a:int , b:int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        remainder = a % b
        return gcdTwoArgs(b,remainder)
    

# When there is 3 Arguements Taken
def gcdThreeArgs(a:int , b:int , c:int) -> int:
    if c == 0:
        gcdTwoArgs(a,b)
    else:
        remainders = gcdTwoArgs(a,b) % c
        return gcdTwoArgs(c,remainders)


# Function for solving the body of infinite Greatest Common Factor
def gcdArguements(numbers, length_Arrays:int) -> int:
    n = 0
    others = []

    # Create var for GCD


    while n < length_Arrays - 1:
        global x
        if n == 0:
            gcdFirst = gcdTwoArgs(numbers[n] , numbers[n+1])
        else:
            gcdOtherwise = gcdTwoArgs(numbers[n+1] , numbers[n+2])
            others.append(gcdOtherwise)

        n += 1
    
    # Solve the numbers separately
    return gcdTwoArgs(gcdFirst,gcdArguements(others,len(others))) # Recursive again cuz there might be Infinite ones






# When there is nth arguement taken
def gcd(*numbers) -> int:
    length_Array = len(numbers)
    # When the length of the tuples which we don't know how many numbers (If it a even Nums)
    if length_Array % 2 == 0:
        return gcdArguements(numbers,length_Array)
    else:
    # When it not even
        oddArray = length_Array -1
        return gcdArguements(numbers,length_Arrays=oddArray)



print(gcd(9,36))