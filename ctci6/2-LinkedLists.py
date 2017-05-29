'''

    Author: Manzoor Mohammed
    URL: https://github.com/manzoormohammed/Python.git

'''

from __future__ import print_function

import sys

class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # LIFO append adds to top
    def append(self, data):
        curr = Node(data)
        if not self.head:
            self.head = curr
        else:
            curr.nextNode = self.head
            self.head = curr
        self.size += 1

    def ouputList(self):
        out = ""
        if self.head:
            curr = self.head
            while curr.nextNode:
                out += str(curr.data) + " -> "
                curr = curr.nextNode
            out += str(curr.data)
        return out


def convertInputToLinkedList(inputList):
    ll = LinkedList()
    for i in range(len(inputList) - 1, -1, -1):
        ll.append(inputList[i])
    print("\nInput = %s" %ll.ouputList())
    print("LinkedList Size = " + str(ll.size))
    return ll


def sol1_removeDups(inputList):
    ll = convertInputToLinkedList(inputList)
    found = []

    def removeDups(currNode):
        if currNode and currNode.data in found:
            removeDups(currNode.nextNode)
        else:
            return currNode

    curr = ll.head
    while curr:
        if curr.data not in found:
            found.append(curr.data)
        curr.nextNode = removeDups(curr.nextNode)
        curr = curr.nextNode
    print("Output = " + ll.ouputList())


def sol2_kLastElement(inputList, k):
    ll = convertInputToLinkedList(inputList)
    if ll.size < k:
        print("value of '" + str(k) + "' for k is greater than LinkedList size")
        return False
    curr = ll.head
    for i in range(ll.size - k):
        curr = curr.nextNode

    print(str(k) + "th element from last is: " + str(curr.data))



def sol3_deleteMiddleNode(inputList):
    ll = convertInputToLinkedList(inputList)

    # Delete 5th node
    try:
        curr = ll.head.nextNode.nextNode.nextNode
    except:
        print("Cannot get to 4th node")
        return False

    try:
        curr.nextNode = curr.nextNode.nextNode
    except:
        print("Cannot delete last node")
        return False

    print("Output = " + ll.ouputList())


# tests
sol1_removeDups([1,2,3,4,2,3,1,1,2,3,4])
sol1_removeDups([1,2,3,4])

sol2_kLastElement([1,2,3,4,5,6,7,8], 3)
sol2_kLastElement([1,2,3,4,5,6,7,8], 9)

sol3_deleteMiddleNode([1,2,3,4,5,6,7,8])
sol3_deleteMiddleNode([1,2,3,4])
