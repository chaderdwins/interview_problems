class Node:
    # default value of data and next_node is none if no data is passed
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # returns data of the node
    def getData(self):
        return self.data

    # set the node data
    def setData(self, data):
        self.data = data

    # get the next node
    def getNext(self):
        return self.next_node

    # set the next node
    def setNext(self, node):
        self.next_node = node

class LinkedList:
    def __init__(self):
        self.head = None

    # inserts a node at the head
    def insertHead(self, data):
        # create a temporary node
        temp_node = Node(data)
        temp_node.setNext(self.head)
        self.head = temp_node
        del temp_node

    # inserts a node at the tail
    def insertTail(self, data):
        start = self.head
        temp_node = Node(data)
        while start.getNext():
            start = start.getNext()
        start.setNext(temp_node)
        del temp_node
        return True

    # prints the linked list
    def print(self):
        start = self.head
        if start is None:
            print("The linked list is currently empty.")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.next_node
            if start:
                print("-->", end=" ")
        print()

    # gives the length of the linked list
    def length(self):
        start = self.head
        size = 0
        while start:
            size += 1
            start = start.getNext()
        # print(size)
        return size

    # finds the index of the given data
    def index(self, data):
        start = self.head
        index = 1

        while start:
            if start.getData() == data:
                return index
            else:
                index += 1
                start = start.getNext()

    # removes an item from the linked list
    # needs to check if data is in list-------------------------------------------------------------------
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNext()

        # if previous is None then the data is found at first index
        if previous is None:
            self.head = start.getNext()
        else:
            previous.setNext(start.getNext())
        return found

    # finds the largest value in the linked list
    def max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNext()
        return largest

    # gives the smallest value in the linked list
    def min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNext()
        return smallest

    # appends data to the end of the linked list
    def append(self, data):
        self.insertTail(data)
        return True

    # deletes and returns the tail of the linked list
    def pop(self):
        start = self.head
        previous = None

        while start.getNext():
            previous = start
            start = start.getNext()

        if previous is None:
            self.head = None
        else:
            previous.setNext(None)
            data = start.getData()
            del start
            return data

    # returns the index of the given node
    def nodeIndex(self, index):
        start = self.head
        index = int(index)
        pos = 1
        while pos != index:
            start = start.getNext()
            pos += 1

        data = start.getData()
        return data

    # copies the linked list
    def copy(self):
        temp = LinkedList()
        start = self.head

        temp.insertHead(start.getData())
        start = start.getNext()

        while start:
            temp.insertTail(start.getData())
            start = start.getNext()

        return temp

    # clears the linked list
    def clear(self):
        self.head = None
        return True

    # deletes and returns a node at the specified index
    def popIndex(self, index):
        data = self.nodeIndex(index)
        self.remove(data)
        return data

    # counts how many of the given value are in a linked list
    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNext()
        return count1

    # reverses the linked list
    def reverse(self):
        start = self.head
        temp_node = None
        previous_node = None

        while start:
            temp_node = start.getNext()
            start.setNext(previous_node)
            previous_node = start
            start = temp_node

        self.head = previous_node
        return True

    # sorts the linked list
    def sort(self):
        start = self.head
        begin_node = start
        while begin_node:
            temp_node = begin_node
            temp_node2 = begin_node
            smallest = begin_node.getData()
            while temp_node:
                if smallest > temp_node.getData():
                    smallest = temp_node.getData()
                    temp_node2 = temp_node
                temp_node = temp_node.getNext()

            # swap data of begin_node and temp_node2
            temp = begin_node.getData()
            begin_node.setData(temp_node2.getData())
            temp_node2.setData(temp)

            begin_node = begin_node.getNext()

    # returns a sorted copy of the original linked list, w/o modifying the original
    def sorted(self):
        start = self.head
        temp_list = self.copy()
        temp_list.sort()
        return temp_list

    # converts the linked list to a list
    def list(self):
        start = self.head
        temp_list = []
        while start:
            temp_data = start.getData()
            temp_list.append(temp_data)
            start = start.getNext()
        return temp_list

    # converts linked list to a set
    def set(self):
        start = self.head
        temp_set = set()
        while start:
            temp_data = start.getData()
            if temp_data not in temp_set:
                temp_set.add(temp_data)
            start = start.getNext()
        return temp_set

    # converts the linked list to a string
    def str(self, seperator=""):
        start = self.head
        new_string = ""
        while start:
            temp_string = start.getData()
            new_string += str(temp_string)
            start = start.getNext()

            # if next node exists only the append seperator
            if start:
                new_string += seperator

        return new_string

# creating LinkedList
myList = LinkedList()

# adding some elements to the start of LinkedList
myList.insertHead(5)
myList.insertHead(4)
myList.insertHead(3)
myList.insertHead(2)
myList.insertHead(1)


myList.print()

# adding some elements to the End of the LinkedList
myList.insertTail(12)
myList.insertTail(13)
myList.insertTail(3)
myList.print()

# printing Length
print(myList.length())

# printing index of an element
print(myList.index(3))

# printing element at a particular index
print(myList.nodeIndex(5))

# removing an element
print(myList.remove(12))

# removing element from a particular index
print("poppin!")
myList.popIndex(2)

myList.print()

# printing max and min element
print(myList.max())
print(myList.min())

# appending and poping elements
print(myList.append(31))
myList.print()
print(myList.pop())
myList.print()

# creating a copy of the linked List
myList2 = myList.copy()
myList2.print()

# removing all elements from the LinkedList
myList2.clear()
myList2.print()


# printing a string of elements of the LinkedList
print(myList.str(","))

# printing count of particular element in the List
print(myList.count(3))

# making a builtIn List from the LinkedList
newList = myList.list()
print(newList)

# making a List from the LinkedList
newSet = myList.set()
print(newSet)

# reversing the linkedLkst
myList.reverse()
myList.print()

# making a sorted LinkedList out of the Original
myList3 = myList.sorted()
myList3.print()

# sorting the LinkedList
myList.sort()
myList.print()
