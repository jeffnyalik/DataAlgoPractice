
## Find Length of a Linked List
"""
Write a function to count the number of nodes in a given singly linked list
"""

"""
We can initialize count as 0.
Initialize node pointer current = head.
Then we can do the following:
 - while current != None
    -current = current -> next
    -increment count by 1
-return count
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

    
    def countNodes(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count +=1
        return count
    
    
    
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
print(ll.countNodes())
ll.printList()
