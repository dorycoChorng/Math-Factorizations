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
    length = len(numbers)
    anotherArray = [] # Array on recursive methods

    # If the length is even
    if length % 2 == 0:
        gcdEven(arrays=numbers,length=length,anotherArray=anotherArray)
        # Look the conditions if the length of another array is 2 or 3
        if len(anotherArray) == 2:
            return gcdTwoArgs(anotherArray[0],anotherArray[1])
        elif len(anotherArray) == 1:
            return gcdTwoArgs(numbers[0],numbers[1])
        elif len(anotherArray) == 3:
            return gcdThreeArgs(anotherArray[0],anotherArray[1],anotherArray[2])
    else:
        # The odd length of the array, so we need to separate the last index and solve the rest of the array
        lengthsOdd = length -1
        gcdEven(arrays=numbers,length=lengthsOdd,anotherArray=anotherArray)
        anotherArray.append(numbers[len(numbers) - 1]) # end index
        if len(anotherArray) == 2:
            return gcdTwoArgs(anotherArray[0],anotherArray[1])
        elif len(anotherArray) == 3:
            return gcdThreeArgs(anotherArray[0],anotherArray[1],anotherArray[2])
       



nums = (8, 12, 20, 45, 67, 89, 12)

print(gcd(nums))