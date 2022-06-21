class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        

class Tree(object):
    
    def __init__(self):
        self.root = None
        
    
    def print(self):
        self.__print(self.root)
    
    def __print(self, curr_node):
        # Recursively print a subtree(in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')
            self.__print(curr_node.right)
        
    
    def insert(self, data):
        y = None # temporary variable to compare with other nodes
        x = self.root # root
        z = Node(data) # New Node
        
        while x is not None:
            y = x;
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        
        z.parent = y;
        if y == None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
            
    
    def min(self):
        
        if self.root is not None:
            x = self.root
            
            while x.left is not None:
                x = x.left
            
            return x.data
        else:
            return None
        
    def __minPointer(self, x = None):
        if self.root is not None:
            if x is None:
                x = self.root
            while x.left is not None:
                x = x.left
            return x
        else:
            return None
    
    def max(self):
        
        if self.root is not None:
            x = self.root
            
            while x.left is not None:
                x = x.right
            
            return x.data
        else:
            return None
        
    def __find_node(self, data):
        x = self.root
        while x is not None and data != x.data:
            if data < x.data:
                x = x.left
            else:
                x = x.right
        return x
    
    def find_node(self, data):
        x = self.root
        while x is not None and data != x.data:
            if data < x.data:
                x = x.left
            else:
                x = x.right
        return x
    
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        
        if v is not None:
            v.parent = u.parent
    
    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree and raise a KeyError
        # If you find the and ...
        #    a) The node has no children, just set it's parent's pointer to Null.
        #    b) The node has one child, make the nodes parent point to its child.
        #    c) The node has two children, replace it with its successor, and remove successor from its previous location.
        
        if self.root == None:
            raise KeyError
        
        z = self.__find_node(data)
        
        if z.left == None:
            self.transplant(z, z.right)
            
        elif z.right == None:
            self.transplant(z, z.left)
            
        else:
            y = self.__minPointer(z.right)
            if y.parent is not z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y
            
        return None

# Driver code
if __name__== '__main__':
    t = Tree()
    
    t.insert(4)
    t.insert(2)
    t.insert(6)
    t.insert(1)
    t.insert(3)
    t.insert(5)
    t.insert(7)
    
    t.delete(4)
    
    t.print()
    