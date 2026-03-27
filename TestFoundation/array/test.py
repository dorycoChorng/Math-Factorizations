# The Cases
caseOne = [1,2]
caseTwo = [1,2,3]
caseThree = [1,2,3,4,5]
caseFour = [22,45,678,12,78,234,87,12,78,123,8,2]


# Enter the code here
def separation(array:list) -> list:
    print(f"DEBUG: Entering separation with array: {array}")
    newArr = []
    length = len(array)
    if length % 2 == 0:
        i = 0
        while i < length/2:
            split = array[:2]
            print(f"DEBUG: Even block - loop {i}, split elements: {split}")
            newArr.append(split[0]+split[1]) # The sum of 2 nums to append in the new array
            array.remove(split[0]) 
            array.remove(split[1])
            array.sort()
            i += 1
        
        print(f"DEBUG: Even block - newArr before next step: {newArr}")
        if len(newArr) > 2:
            array.clear()
            array = newArr.copy()
            newArr.clear()
            return separation(array)
        elif len(newArr) == 1:
            return newArr
        else:
            sum = newArr[0] + newArr[1]
            array.clear()
            array.append(sum)
            print(f"DEBUG: Even block - returning sum: {array}")
            return array
    
    # when odd
    else:
        lens = (length-1)/2 # The length for odd
        endIndex = array[length-1]
        print(f"DEBUG: Odd block - endIndex: {endIndex}")
        firstArray = array.copy()
        firstArray.remove(endIndex)
        firstIndexes = separation(firstArray)
        firstIndexes.append(endIndex)
        array.clear()
        array.append(firstIndexes[0]+firstIndexes[1])
        print(f"DEBUG: Odd block - returning sum: {array}")
        return array
    

print(separation(caseOne))
print(separation(caseTwo))
print(separation(caseThree))
print(separation(caseFour))
