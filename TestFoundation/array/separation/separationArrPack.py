import os
import sys

# Ensure root package path is on sys.path when executing from nested folder.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import gcdPackage as gcdpkg
gcds = gcdpkg.gcds()

class separationArray:
    def __init__(self, array: list):
        self.array = list(array) # Make the array self in the class

    def separation(self) -> list:
        # Variable
        arrays = list(self.array)
        newArr = []
        length = len(arrays)

        # When the array length is even

        if length % 2 == 0:
            i = 0
            while i < length / 2:
                split = arrays[:2]
                newArr.append(gcds.gcdTwoArgs(split[0], split[1]))
                arrays.remove(split[0])
                arrays.remove(split[1])
                arrays.sort()
                i += 1

            # If it still large and do another recursive for simple terms
            if len(newArr) > 2:
                return separationArray(newArr).separation()
            elif len(newArr) == 1:
                return newArr
            else:
                gcD = gcds.gcdTwoArgs(newArr[0], newArr[1])
                arrays = [gcD]
                return arrays

    # When the array length is odd

        else:
            endIndex = arrays[-1] # Value of the last index
            somearr = arrays[:-1] # Remove the last index
            firstIndexes = separationArray(somearr).separation() # Put the remain indexes to recursive
            firstIndexes.append(endIndex) # Add it back for final touch
            arrays = [gcds.gcdTwoArgs(firstIndexes[0], firstIndexes[1])]
            return arrays


# Print
main = separationArray([8,4,36,12,72,42,52]).separation()
print(main)

