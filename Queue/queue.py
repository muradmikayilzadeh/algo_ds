class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self,data):
        newNode = Node(data)
        
        if self.rear == None:
            self.front = self.rear = newNode
            print("Enqueued")
            return
        
        self.rear.next = newNode
        self.rear = newNode
        print("Enqueued")
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next
        
        if self.front == None:
            self.rear = None
        return temp.data
    
if __name__== '__main__':
    q = Queue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())