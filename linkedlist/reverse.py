
"""
Given a pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes.

Examples: 

Input: Head of following linked list 
1->2->3->4->NULL 
Output: Linked list should be changed to, 
4->3->2->1->NULL

Input: Head of following linked list 
1->2->3->4->5->NULL 
Output: Linked list should be changed to, 
5->4->3->2->1->NULL

Input: NULL 
Output: NULL

Input: 1->NULL 
Output: 1->NULL 
"""

"""
We need to initialize three pointers:
next as None.
prev as None.
curr as head
We can iterate through the linkedlist and do the following:
Before changing the next of the curr,we need to store the next node.
next = curr -> next
update the next pointer of curr to prev
curr ->next = prev
update previous as curr and curr as next
prev = curr
curr = next
Make head as the prev
head = prev
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

    
    def reverse(self):
        curr = self.head
        prev = None
        next = None

        while curr !=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev
  
    
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

ll.reverse()
ll.printList()
