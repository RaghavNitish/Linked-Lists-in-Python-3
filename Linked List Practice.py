#!/usr/bin/env python
# coding: utf-8

# # Linked List Practice
# 
# Implement a linked list class. You have to define a few functions that perform the desirbale action. Your `LinkedList` class should be able to:
# 
# + Append data to the tail of the list and prepend to the head
# + Search the linked list for a value and return the node
# + Remove a node
# + Pop, which means to return the first node's value and delete the node from the list
# + Insert data at some position in the list
# + Return the size (length) of the linked list

# In[77]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# In[78]:


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


# #### Task 1. Write definition of `prepend()` function and test its functionality

# In[79]:


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head == None:
        self.head = Node(value)
    else:
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
    return 


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend


# <div id="spoiler_1" style="display:none">
# Here is an example of a Makefile you could create for this exercise:
# ```
# cmd1:
#         @echo "$@"
# 
# cmd2:
#         @echo "$@"
# 
# all: cmd1 cmd2
# ```
# 
# Note that after `cmd1` and `cmd2`, and before `@echo`, should be a tab. The `@` at the start of these lines prevents `make` from automatically printing the lines, while `"$@"` is the variable for a string containing the target name, in this case either `cmd1` or `cmd2`. To double-check that `make` is actually showing the command name from within the command itself, try to `echo` something else from within one of them, such as `Hello World!`, and check the results.
# </div>
# <button title="Click to show/hide content" type="button" onclick="if(document.getElementById('spoiler_1') .style.display=='none') {document.getElementById('spoiler_1') .style.display=''}else{document.getElementById('spoiler_1') .style.display='none'}">Show Solution</button>
# 
# ```{toggle} Click the button o your right to reveal the solution!
# 
# def prepend(self, value):
#     """ Prepend a node to the beginning of the list """
# 
#     if self.head is None:
#         self.head = Node(value)
#         return
# 
#     new_head = Node(value)
#     new_head.next = self.head
#     self.head = new_head
# ```

# In[80]:


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


# #### Task 2. Write definition of `append()` function and test its functionality

# In[81]:


def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if self.head == None:
        self.head = Node(value)
        
    else:
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        
        current_node.next = Node(value)

LinkedList.append = append


# In[82]:


# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"


# In[83]:


# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"


# #### Task 3. Write definition of `search()` function and test its functionality

# In[84]:


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    if self.head == None:
        return self.head
    else:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

LinkedList.search = search


# In[85]:


# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


# #### Task 4. Write definition of `remove()` function and test its functionality

# In[86]:


def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write  function to remove here
    
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


# In[87]:


# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"


# #### Task 5. Write definition of `pop()` function and test its functionality

# In[88]:


def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    value = self.head.value
    temp = self.head
    
    self.head = self.head.next
    
    temp.next = None
    temp.value = None
    
    return value

LinkedList.pop = pop


# In[89]:


# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


# #### Task 6. Write definition of `insert()` function and test its functionality

# In[90]:


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here 
    if pos > len(linked_list.to_list()) - 1:
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


# In[91]:


# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"


# #### Task 7. Write definition of `size()` function and test its functionality

# In[94]:


def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    return len(linked_list.to_list())

LinkedList.size = size


# In[95]:


# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"


# <span class="graffiti-highlight graffiti-id_1vt6pt0-id_q7rr1km"><i></i><button>Show Solution</button></span>
