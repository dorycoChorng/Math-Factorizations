import os
import sys

# Ensure root package path is on sys.path when executing from nested folder.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import gcdPackage as gcdpkg
gcds = gcdpkg.gcds()

class separationArray:
    def __init__(self, array: list):
        self.array = list(array)

    def separation(self) -> list:
        arrays = list(self.array)
        newArr = []
        length = len(arrays)

        if length % 2 == 0:
            i = 0
            while i < length // 2:
                split = arrays[:2]
                newArr.append(gcds.gcdTwoArgs(split[0], split[1]))
                arrays.remove(split[0])
                arrays.remove(split[1])
                arrays.sort()
                i += 1

            if len(newArr) > 2:
                return separationArray(newArr).separation()
            elif len(newArr) == 1:
                return newArr
            else:
                gcD = gcds.gcdTwoArgs(newArr[0], newArr[1])
                arrays = [gcD]
                return arrays

        else:
            endIndex = arrays[-1]
            firstArray = arrays[:-1]
            firstIndexes = separationArray(firstArray).separation()
            firstIndexes.append(endIndex)
            arrays = [gcds.gcdTwoArgs(firstIndexes[0], firstIndexes[1])]
            return arrays


# Print
main = separationArray([11, 121]).separation()
print(main)
