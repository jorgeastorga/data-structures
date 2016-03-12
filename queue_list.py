"""
Create a Queue of elemenets that exercises the functions of the queue
class above.

#Cafeteria Line (modeled as a Queue)
>>> cafeteriaLine = Queue()

>>> type(cafeteriaLine)
<class 'queue_list.Queue'>

#Add an item to the queue and make sure it returns the list
>>> cafeLine = cafeteriaLine.queue("Jorge")
>>> print(cafeLine)
['Jorge']


#Test the cafeteria line queue for being empty

>>> lineEmpty = cafeteriaLine.isEmpty()
>>> if lineEmpty == True:
...     print("There is no line at the cefeteria")
... else:
...     print("There are customers waiting in line")
There are customers waiting in line


#Remove an person from the cafeteria line
>>> personServed =  cafeteriaLine.dequeue()
>>> print(personServed)
Jorge

#Test the cafeteria line queue for being empty
>>> lineEmpty = cafeteriaLine.isEmpty()

>>> if lineEmpty == True:
...     print("There is no line at the cefeteria")
... else:
...     print("There are customers waiting in line")
There is no line at the cefeteria
"""


# The purpose of this class is to implement a Queue
#using the list data structure in Python

class Queue:
    def __init__(self):
        self.queueList = list()

    def queue(self, x):
        self.queueList.append(x)
        return self.queueList

    def dequeue(self):
        item = self.queueList[0]
        del(self.queueList[0])
        return item

    def isEmpty(self):
        queueLength = len(self.queueList)
        if queueLength == 0:
            return True
        else:
            return False
