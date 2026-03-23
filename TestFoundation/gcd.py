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
    # length_Array = len(numbers)
    # # When the length of the tuples which we don't know how many numbers (If it a even Nums)
    # if length_Array % 2 == 0:
    #     return gcdArguements(numbers,length_Array)
    # else:
    # # When it not even
    #     oddArray = length_Array -1
    #     return gcdArguements(numbers,length_Arrays=oddArray)

    length = len(numbers)
    anotherArray = [] # Array on recursive methods
    if length % 2 == 0:
        gcdEven(arrays=numbers,length=length,anotherArray=anotherArray)
        return anotherArray
    else:
        lengthsOdd = length -1
        gcdEven(arrays=numbers,length=lengthsOdd,anotherArray=anotherArray)
        anotherArray.append(numbers[len(numbers) - 1]) # end index



print(gcd(8,12,12,45,78,234,12))