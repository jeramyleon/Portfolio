class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeB.prev = nodeA
nodeC.next = nodeD
nodeC.prev = nodeB
nodeD.next = nodeE
nodeD.prev = nodeC
nodeE.prev = nodeD

def countNodes(head): # return the number of nodes in linked list
    count = 1

    while head.next:
        count += 1 
        head = head.next
    
    return count

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 
    
class Linkedlist:
    def __init__(self):
        self.head = None 
    
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head 
            while current.next:
                current = current.next
            current.next = newNode 
        else:
            self.head = newNode 
    
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

jeramy = Linkedlist()
jeramy.insert(1)
jeramy.insert(2)
jeramy.insert(3)
jeramy.insert(4)
jeramy.printLL()


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next 
            current.next = newNode 
        else:
            self.head = newNode 
    
    def printLL(self):
        current = self.head 
        while current:
            print(current.data)
            current = current.next 

kanye = Linkedlist()
kanye.insert("College Dropout")
kanye.insert("Late Registration")
kanye.insert("Graduation")
kanye.insert("808s & Heartbreak")
kanye.insert("My Beautiful Dark Twisted Fantasy")
kanye.printLL()


