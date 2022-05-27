class StackNode:
    
    #Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top == None
    
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode
        print("% d pushed to stack" %(data))
        
    def pop(self):
        if (self.isEmpty()):
            print("Operation cancelled. Stack is empty")
            return float("-inf")
        temp = self.top
        self.top = temp.next
        popped = temp.data
        return popped
    
    def peek(self):
        if (self.isEmpty()):
            print("Operation cancelled. Stack is empty")
            return float("-inf")
        return self.top.data
    
if __name__=='__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())