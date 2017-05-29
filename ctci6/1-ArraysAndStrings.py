'''

    Author: Manzoor Mohammed
    URL: https://github.com/manzoormohammed/Python.git

'''

from __future__ import print_function

import sys


# print error and stop execution with failure
def printerror(message):
    print("ERROR: " + message, file=sys.stderr)
    sys.exit(1)

def sol1_isUnique(inputString):
    foundChars = {}
    for char in inputString:
        try:
            if foundChars[char]:
                return False
        except:
            pass
        foundChars[char] = "found"
    return True


def sol2_checkPermutation(string1, string2):
    for char in string1:
        if char not in string2:
            return False
        string2 = string2.replace(char, "", 1)
    return True


def sol3_URLify(inputString, trueLength):
    index = len(inputString) - 1
    output = list(inputString)
    for i in range(trueLength - 1, 0, -1):
        if inputString[i] == " ":
            output[index] = "0"
            output[index - 1] = "2"
            output[index -2] = "%"
            index -= 2
        else:
            output[index] = inputString[i]
        index -=1

    return "".join(output)


def sol4_palindromePermutation(inputString):
    charCounts = {}
    for char in inputString:
        if char == " ":
            continue
        if char in charCounts:
            charCounts[char] += 1
        else:
            charCounts[char] = 1

    foundOddCharCount = False
    for charKey in charCounts:
        if charCounts[charKey] % 2 != 0:
            if foundOddCharCount:
                return False
            else:
                foundOddCharCount = True

    return foundOddCharCount


def sol5_oneAway(string1, string2):
    def isOneAway(string1, string2):
        string1AsciiTotal = 0
        for char in string1.lower():
            string1AsciiTotal += ord(char)
        string2AsciiTotal = 0
        for char in string2.lower():
            string2AsciiTotal += ord(char)
        delta = abs(string1AsciiTotal - string2AsciiTotal)
        if delta >= ord("a") and delta <= ord("z"):
            return True
        else:
            return False

    if len(string1) == len(string2):
        return isOneAway(string1, string2)
    else:
        if abs(len(string1) - len(string2)) == 1:
            return isOneAway(string1, string2)
        else:
            return False


def sol6_stringCompression(inputString):
    output = ""
    count = 1
    for i in range(len(inputString)):
        if (i != len(inputString) - 1) and inputString[i] == inputString[i + 1]:
            count += 1
        else:
            output += inputString[i] + str(count)
            count = 1

    if len(inputString) < len(output):
        return inputString
    else:
        return output


def sol7_rotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(len(matrix)):
        print(matrix[i])


def sol8_zeroMatrix(matrix):
    rowsToSetZero = []
    colsToSetZero = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rowsToSetZero.append(i)
                colsToSetZero.append(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rowsToSetZero or j in colsToSetZero:
                matrix[i][j] = 0

    for i in range(len(matrix)):
        print(matrix[i])


def sol9_stringRotation(string1, string2):
    return string1 in (string2 + string2)


# execute as standalone program to test
if __name__ == "__main__":
    print(sol1_isUnique("avew31d"))
    print(sol1_isUnique("avew31da"))

    print(sol2_checkPermutation("fbacgde", "abcdefg"))
    print(sol2_checkPermutation("fbacgdh", "abcdefg"))

    print(sol3_URLify("My Test URL    ", 11))

    print(sol4_palindromePermutation("manz man"))
    print(sol4_palindromePermutation("manz manz"))

    print(sol5_oneAway("the", "then"))
    print(sol5_oneAway("this", "then"))

    print(sol6_stringCompression("aaabbcccccd"))
    print(sol6_stringCompression("abdwq"))

    sol7_rotateMatrix([[1,2,3], [4,5,6], [7,8,9]])

    sol8_zeroMatrix([[1, 2, 0], [4, 0, 6], [7, 8, 9]])

    print(sol9_stringRotation("mytest", "testmy"))
    print(sol9_stringRotation("mytest", "testmyfail"))