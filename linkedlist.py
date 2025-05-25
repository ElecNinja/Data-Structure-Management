class Node:
    def __init__(self, data):
        self.data = data  # store item
        self.next = None  # pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None  # start with empty list

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # first item
        else:
            current = self.head
            while current.next:
                current = current.next  # go to last node
            current.next = new_node
    
    def get(self, index):  # get item at specific index
        if index < 0:  # invalid index
            return None
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next  # move pointer
        
        if current:  # if current is not None
            return current.data  # return item data
        else:
            return -1  # out of range

    def insert_at(self, index, data): # insert at specific index
        if index < 0: # invalid index
            return None
        new_node = Node(data)
        if index == 0: # insert at head
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                break
            current = current.next # move pointer till index - 1
        
        new_node.next = current.next # insert after current
        current.next = new_node # link new node

    def remove_at(self, index): # remove node at specific index
        if index < 0:
            return None

        current = self.head
        if index == 0: # remove head
            self.head = current.next
            return current.data

        prev = None
        for _ in range(index):
            if current is None:
                return None  # out of range
        prev = current
        current = current.next

        if current is None:
            return None  # out of range current.next after loop

        prev.next = current.next
        return current # return removed node for stack undo


    def display(self):
        current = self.head
        while current:
            print(current.data)   # print item data
            current = current.next
        
    
    def to_list(self): # convert linked list to python list
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def getIndex(self, id): # get index of item by id
        current = self.head
        index = 0
        while current:
            if current.data.id == id:
                return index
            current = current.next
            index += 1
        return -1
    
    def size(self): # get number of items in linked list
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
