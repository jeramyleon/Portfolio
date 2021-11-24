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

    while head.next is not None:
        count += 1 
        head = head.next
    
    return count
 



    
     