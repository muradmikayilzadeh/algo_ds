class PriorityQueueNode:
    
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None
        
class PriorityQueue:
    
    def __init__(self):
        self.front = None
        
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, value, pr):
        
        if self.isEmpty() == True:
            self.front = PriorityQueueNode(value, pr)
            print("Enqueued!");
            return 1
        
        else:
            if self.front.priority > pr:
                
                newNode = PriorityQueueNode(value, pr)
                newNode.next = self.front
                self.front = newNode
                return 1
            
            else:
                temp = self.front
                
                while temp.next:
                    if pr <= temp.next.priority:
                        break
                
                    temp = temp.next
            
                newNode = PriorityQueueNode(value, pr)
                newNode.next = temp.next
                temp.next = newNode
                    
                return 1
    
    def dequeue(self):
        
        if self.isEmpty() == True:
            return
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
        
    def peek(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front.data
        
    def traverse(self):
        if self.isEmpty() == True:
            return "Queue is Empty!"
        else:
            temp = self.front
            
            while temp:
                print(temp.data, end="->")
                temp = temp.next
                
if __name__ == "__main__":
    
    pq = PriorityQueue()
    
    pq.enqueue(4,1)
    pq.enqueue(5,2)
    pq.enqueue(6,3)
    pq.dequeue()
    pq.enqueue(7,0)
    
    pq.traverse()
        