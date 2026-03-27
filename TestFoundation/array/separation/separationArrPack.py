# import
from ..TestFoundation import gcdPackage as gcds

class separationArray:
    def _init_(self,array:list):
        self.array = array

    def separation(self) -> list:
        arrays = self.array
        length = len(arrays)
        if length % 2 == 0:
            i = 0
            while i < length/2:
                split = arrays[:2]
                newArr.append(gcds.gcdTwoArgs(split[0],split[1])) # The gcd of 2 nums to append in the new array
                arrays.remove(split[0]) 
                arrays.remove(split[1])
                arrays.sort()
                i += 1
            
            if len(newArr) > 2:
                arrays.clear()
                arrays = newArr.copy()
                newArr.clear()
                return separation(arrays)
            elif len(newArr) == 1:
                return newArr
            else:
                gcD = gcds.gcdTwoArgs(newArr[0],newArr[1])
                arrays.clear()
                arrays.append(gcD)
                return arrays
        
        # when odd
        else:
            lens = (length-1)/2 # The length for odd
            endIndex = arrays[length-1]
            firstArray = arrays.copy()
            firstArray.remove(endIndex)
            firstIndexes = separation(firstArray)
            firstIndexes.append(endIndex)
            arrays.clear()
            arrays.append(gcds.gcdTwoArgs(firstIndexes[0],firstIndexes[1]))
            return arrays
    

# Print

main = separationArray.separation([8,9])
print(main)