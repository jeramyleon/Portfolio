class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

def countNodes(head): # return the number of nodes in linked list
    count = 1

    while head.next is not None:
        count += 1 
        head = head.next
    
    return count




    
     