"""
A new node in a linkedlist can be inserted in the following position:
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


"""
To insert a node after a given node:
1. Check if the given node exist or not
   -if the give node does not exist, then terminate the proces
2. If the given node exist, then do the following
   -Make the element to be inserted as the new node
   -change next of the new node to next of the given node
   -shift next of the given node to new node
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

    def addAfterNode(self, givenNode, data):
        if not givenNode:
            print("The given node does not exist")
            return
        new_node = Node(data)
        new_node.next = givenNode.next
        givenNode.next = new_node



    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

ll = LinkedList()
ll.addFront(10)
ll.addFront(20)
ll.addFront(30)

ll.addAfterNode(ll.head.next, 120)
ll.printList()