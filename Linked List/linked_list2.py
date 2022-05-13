class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    #This function inserts a new node at the beginning
    def push(self, new_data):
        
        #Create new node with given new_data
        new_node = Node(new_data)
        
        #Make next of new node as head
        new_node.next = self.head
        
        #Move the head to point to new node
        self.head = new_node
        
    def insertAfter(self, prev_node, new_data):
        
        # check if the given prev_node exists
        if prev_node is None:
            print("The given prev_node must be in LinkedList")
            return
            
        # create new_node and put in the data
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
        
    def append(self, new_data):
        # create new node
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        # else traverse till the last node
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        
    def deleteNode(self, key):
        
        temp = self.head
        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None
        
    #This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
if __name__=='__main__':
    llist = LinkedList()
    llist.printList()
    
    llist.append(1)
    llist.append(2)
    llist.append(3)
    
    llist.deleteNode(3)
    
    llist.printList()
    