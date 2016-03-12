'''The purpose of this class is to implement a stack data
structure using a list (contruct) in Python'''

class Stack:

    def __init__(self):
        self.stackList = list()

    def push(self, x):
        self.stackList.append(x)
        return self.stackList

    def pop(self):
        listLength = len(self.stackList)
        poppedValue = self.stackList[listLength-1]
        del(self.stackList[listLength-1])
        return poppedValue

    def empty(self):
        if len(self.stackList) == 0:
            return True
        else:
            return False
