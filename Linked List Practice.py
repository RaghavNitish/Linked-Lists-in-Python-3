class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Defining a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    if self.head == None:
        self.head = Node(value)
    else:
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
    return 


LinkedList.prepend = prepend

def append(self, value):
    """ Append a value to the end of the list. """       
    if self.head == None:
        self.head = Node(value)
        
    else:
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = Node(value)

LinkedList.append = append

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head == None:
        return self.head
    else:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

LinkedList.search = search

def remove(self, value):
    """ Remove first occurrence of value. """
    
    #Special case
    if self.head.value == value:
        temp = self.head
        self.head = self.head.next 
        
        temp.next = None
        temp.value = 0
        
    else:
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                temp = current_node.next
                current_node.next = temp.next

                #setting the values
                temp.next = None
                temp.value = None

                return
            current_node = current_node.next

LinkedList.remove = remove

def pop(self):
    """ Return the first node's value and remove it from the list. """
    value = self.head.value
    temp = self.head
    
    self.head = self.head.next
    
    temp.next = None
    temp.value = None
    
    return value

LinkedList.pop = pop

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    if pos > len(self.to_list()) - 1:
        #append to the end
        current_node = self.head
        
        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = Node(value)
    else:
        #append at the desired location
        
        #special case
        if pos == 0:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        else:
            count = 0
            current_node = self.head
            
            while current_node.next != None:
                if count == pos - 1:
                    temp = current_node.next
                    temp1 = Node(value)
                    current_node.next = temp1
                    temp1.next = temp
                    return
                    
                current_node = current_node.next 
                count += 1
    return

LinkedList.insert = insert

def size(self):
    """ Return the size or length of the linked list. """
    return len(self.to_list())

LinkedList.size = size