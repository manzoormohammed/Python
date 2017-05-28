'''

    Author: Manzoor Mohammed
    URL: https://github.com/manzoormohammed/Python.git
    
    Find min operations needed to enter a pattern on dialpad

    DialPad: 
        1   2   3
        4   5   6
        7   8   9
        *   0   #
        
    Operations:
            U
        L   S   R
            D
    
    Starts at 1
'''

from __future__ import print_function

import sys


# print error and stop execution with failure
def printerror(message):
    print("ERROR: " + message, file=sys.stderr)
    sys.exit(1)

# hashmap of the dialpad
def getDialPad():
    dialPad = {}
    dialPad["1"] = {"row": 0, "col": 0}
    dialPad["2"] = {"row": 0, "col": 1}
    dialPad["3"] = {"row": 0, "col": 2}
    dialPad["4"] = {"row": 1, "col": 0}
    dialPad["5"] = {"row": 1, "col": 1}
    dialPad["6"] = {"row": 1, "col": 2}
    dialPad["7"] = {"row": 2, "col": 0}
    dialPad["8"] = {"row": 2, "col": 1}
    dialPad["9"] = {"row": 2, "col": 2}
    dialPad["*"] = {"row": 3, "col": 0}
    dialPad["0"] = {"row": 3, "col": 1}
    dialPad["#"] = {"row": 3, "col": 2}
    return dialPad


def operationsCount(char, startAt, dialPad):
    rowDiff = abs(dialPad[char]["row"] - dialPad[startAt]["row"])
    colDiff = abs(dialPad[char]["col"] - dialPad[startAt]["col"])
    return rowDiff + colDiff


def minOperations(inputString):
    if not inputString:
        printerror("Please provide an input string")

    dialPad = getDialPad()
    startAt = "1"
    totalOperations = 0
    for char in inputString:
        if char not in dialPad:
            printerror("Input character '" + char + "' not found in dialPad")

        if char != startAt:
            totalOperations += operationsCount(char, startAt, dialPad)

        # add 1 for operation S (to select)
        totalOperations += 1
        startAt = char

    return totalOperations


# execute as standalone program to test
if __name__ == "__main__":
    print(minOperations("1153*"))

