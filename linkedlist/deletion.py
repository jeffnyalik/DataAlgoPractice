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
        
    def deleteLastNode(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None
    
    def deleteNodeAtPosition(self, position):
        if position < 1:
            print("Position cannot be less than 1")
        elif(position == 1 and self.head != None):
            nodeDelete = self.head
            self.head = self.head.next
            nodeDelete = None

        else:
            temp = self.head
            for i in range(1, position - 1):
                if temp != None:
                    temp = temp.next
            if temp != None  and  temp.next !=None:
                nodeDelete = temp.next
                temp.next = temp.next.next
                nodeDelete = None
            else:
                print("The node is already null")


    def deleteAllNodes(self):
        while self.head !=None:
            temp = self.head
            self.head = self.head.next
            temp = None
    
    def deleteEvenNode(self):
        if self.head != None:
            temp = self.head
            oddNode = self.head
            evenNode = self.head.next
            temp = None

        
        while oddNode !=None and evenNode !=None:
            oddNode.next = evenNode.next
            evenNode = None

            oddNode = oddNode.next
            if oddNode != None:
                evenNode = oddNode.next
    
    def deleteOddNodes(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
            if self.head != None:
                evenNode = self.head
                oddNode = self.head.next

                while evenNode !=None and oddNode !=None:
                    evenNode.next = oddNode.next
                    oddnode = None

                    evenNode = evenNode.next
                    if evenNode != None:
                        oddNode = evenNode.next

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
ll.addFront(40)
ll.addFront(60)
ll.addFront(9)

# ll.popFront()
# ll.deleteLastNode()
# ll.deleteNodeAtPosition(2)
# ll.deleteAllNodes()
# ll.deleteEvenNode()
ll.deleteOddNodes()
ll.printList()
