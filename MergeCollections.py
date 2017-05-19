# Merge Collections

'''

    Author: Manzoor Mohammed
    URL: https://github.com/manzoormohammed/Python.git
    
    To merge collections of dicts or lists without overwriting
    dict.update method of python overwrites the keys which is why this method will be used
    :param c1: dict or list
    :param c2: dict or list
    :return: merged dict of all unique keys in c1 and c2

    Assumption:
        Both inputs are of the same data type (either dict or list)
    
    Example:
        data1 = { "Customer1" : { "Name" : "Best Customer" } }
        data2 = { "Customer1" : { "Address" : "Planet Earth" } }

        dict.update will result in {'Customer1': {'Address': 'Planet Earth'}}

        using this merge method will result in {'Customer1': {'Name': 'Best Customer', 'Address': 'Planet Earth'}}

'''

from __future__ import print_function

import copy
import sys


# print error and stop execution with failure
def printerror(message):
    print("ERROR: " + message, file=sys.stderr)
    sys.exit(1)


def merge(c1, c2): # c1 and c2 are our collections of same data type

    if type(c1) != type(c2):
        printerror("Data types for input do not match")

    # Iterate through all keys in c2
    for indx, keyName in enumerate(c2):
        # keyName doesn't exist in c1 so add it
        if keyName not in c1:
            if type(c1) == type({}):
                c1[keyName] = c2[keyName]
            elif type(c1) == type([]):
                if type(c2[indx]) == type({}) or type(c2[indx]) == type([]):
                    merge(c1[indx], c2[indx])
                elif c2[indx] not in c1:
                    c1.append(c2[indx])

        # keyName value is a list so iterate over that list
        elif type(c1[keyName]) == type([]) and type(c2[keyName]) == type([]):
            merge(c1[keyName], c2[keyName])

        # keyName value is a dict so iterate over that dict
        elif type(c1[keyName]) == type({}) and type(c2[keyName]) == type({}):
            merge(c1[keyName], c2[keyName])

        # if keyName matches what was it c1 but the value is diff, I choose to throw an error.
        # Can easily change this implementation to update the keyName with the new value if that option is needed.
        elif c1[keyName] != c2[keyName]:
            printerror("Duplicate key '" + keyName + "' with diff values '" +
                  c1[keyName] + "' and '" + c2[keyName] + "' cannot be resolved.")

    # Will return merged collection if no errors occured
    return c1


def test_merge(data1={}, data2={}):
    '''
    Test my data collections data1 and data2. Will use sample data if no input is received
    :param data1: dict or list
    :param data2: dict or list
    :return: merge of data1 and data2
    '''

    if data1 == {} and data2 == {}: # No input was provided
        data1 = { "Customer1" : { "Name" : "Best Customer" } }
        data2 = { "Customer1" : { "Address" : "Planet Earth" } }

    print("data1 = " + str(data1))
    print("data2 = " + str(data2))

    # Create a copy of data1 so we don't alter our original collection
    data1Copy = copy.deepcopy(data1)
    data1Copy.update(data2)
    print("data1.update(data2) would produce : " + str(data1Copy))

    print ("merge(data1, data2) will produce: " + str(merge(data1, data2)))


# execute as standalone program to test
if __name__ == "__main__":
    test_merge()

