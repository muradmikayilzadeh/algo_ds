#Node class

class Node:
    
    #Function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
        

class LinkedList:
    
    #Function to initialize the Linked List object
    def __init__(self):
        self.head = None
        
    #This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
                

if __name__=='__main__':
    
    #Creating Nodes
    firstNode = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)
    
    '''
    Three nodes have been created.
  
        one             second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    
    
    #Start linked list
    llist = LinkedList()
    llist.head = firstNode
    
    '''
    Three nodes have been created.
  
    llist.head          second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    
    llist.head.next = secondNode
    
    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    secondNode.next = thirdNode
     
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    
    llist.printList()
    