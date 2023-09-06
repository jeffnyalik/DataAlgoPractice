"""
Linkedlist deletion
A node in a linkedlist can be deleted in the following areas:
1. from the beginning
2. the last node
3. at a given position
4. deletion of all nodes

"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def popFront(self):
        if self.head !=None:
            temp = self.head
            self.head = self.head.next ## move head to next of head
            temp = None ## Free up the memory

    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

ll = LinkedList()
ll.addFront(10)
ll.addFront(20)
ll.addFront(30)
ll.addFront(50)

ll.popFront()
ll.printList()
