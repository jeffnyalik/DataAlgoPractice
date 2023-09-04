"""
A new node in a linkedlist can be inserted the following position
1. At the front of the linkedlist.
2. After a given node
3. At the end of the linkedlist
"""

"""
To insert a node at the front:
1. Make the first node of the linkedlist to a new node
2. Remove the original node from the head of the linkedlist
3. Make the new node as the head of the linkedlist
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


    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

ll = LinkedList()
ll.addFront(10)
ll.addFront(20)
ll.addFront(30)
ll.printList()