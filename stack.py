class Stack:
    def __init__(self):
        self.items = []  # use a list to store stack elements

    def push(self, item):
        self.items.append(item)  # add to the top

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()  # remove from the top

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]  # see the top item (-1 returns the last item)

    def is_empty(self):
        return len(self.items) == 0  # check if stack is empty

    def size(self):
        return len(self.items) # get the number of items in the stack
    
