from stack_list import Stack
from queue_list import Queue

#Use the stack to simulate a zoo
zoo = Stack()

zooList = zoo.push("Monkey") #add a monkey
zooList = zoo.push("Tiger")  #add a Tiger
zooList = zoo.push("Zebra")  #add a Zebra, now we're in business
print(zooList)

zooStatus = zoo.empty() # is the zoo empty at the moment

if zooStatus is True:
    print("The zoo is empty")
elif zooStatus is False:
    print("The zoo is not empty")
else:
    print("The zoo is in a weird state. Check back later. ")


#Use the queue to simulate a line at the coffee shop
coffeeLine = Queue()
