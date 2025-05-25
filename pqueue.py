class Queue:
    def __init__(self):
        self.items = []  # list to store items

    def enqueue(self, item):
        self.items.append(item)  # add to the back

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)  # remove from the front

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]  # see the front item

    def is_empty(self):
        return len(self.items) == 0 # check if queue is empty

    def size(self):
        return len(self.items) # get the number of items in queue
    
    def getIndex(self, item):
        return self.items.index(item) # get index of item in queue
       
