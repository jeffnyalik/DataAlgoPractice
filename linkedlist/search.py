"""
Search an element in a linkedlist.
An alement in a linkedlist can be searched both recursive and iteratively
"""

"""
Given a linked list and a key ‘X‘ in, the task is to check if X is present in the linked list or not. 

Examples:

Input: 14->21->11->30->10, X = 14
Output: Yes
Explanation: 14 is present in the linked list.

Input: 6->21->17->30->10->8, X = 13
Output: No
"""

"""
Option one:
1. We can create a vector to store the node values
2. Then we can check if the key value exist in the vector or not
3. We return True or 1 if exists, otherwise we return False or -1

NB: Space complexity will be O(N) since we are using an extra datastructure vector, time will also be O(N) to traverse the list

"""

"""
Option Two:
1. We can initialize a node pointer current
2. If the current value is equal to the key being searched,then we can true, otherwise move to the next node,
   if the key is not found, return False

NB: Space complexity will be O(1) since we are not using an extra datastructure, time will be O(N) to traverse the list.
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

    
    def searchKey(self, key):
        res = []
        temp = self.head
        while temp:
            res.append(temp.data)
            temp = temp.next
        if key in res:
            return True
        return False
    
    
    def searchKeyTwo(self, key):
        current = self.head
        while current != None:
            if current.data == key:
                return True
            current = current.next
        return False
    
    


    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

ll = LinkedList()
ll.addFront(10)
ll.addFront(20)
ll.addFront(30)

# print(ll.searchKey(10))
print(ll.searchKeyTwo(400))
ll.printList()
