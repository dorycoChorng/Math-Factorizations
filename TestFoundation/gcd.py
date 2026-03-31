'''
This file is demonstrate of greatest common factor in the mathematics computationally
*** Theory of the greatest common factor in computer science theory ***
If A = 0 , so GCD(A,B) = B. If, B = 0; This will be vice versa
Let say: A is a quotient equation (A = B*y + R); Then GCD(A,B) = GCD(B,R)
** Using Recursive Method **

'''



import time

from TestFoundation.array.separation.separationArrPack import separationArray

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

# Function for solving the arguments evenly
def gcdEven(arrays:list , length:int , anotherArray:list) ->list:
    # arrays --> The original array
    # anotherArray --> The another array 
    i = 0
    separate = length / 2
    while i < separate:
        split = arrays[:2]
        anotherArray.append(gcdTwoArgs(split[0],split[1]))

        listArr = list(arrays) # Convert Tuple to Array
        listArr.remove(split[0])
        listArr.remove(split[1])
        listArr.sort()
        list(split).clear()
        i +=1
    return anotherArray


# When there is nth arguement taken
def gcd(*numbers) -> int:
    # Use separationArray class from package
    separation = separationArray(numbers)
    
    returning = separation.separation() # Turn the value array as a list
    return returning[0]



print(gcd([12,24]))