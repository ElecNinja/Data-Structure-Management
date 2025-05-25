from item import Item

class BSTNode:
    def __init__(self, item: Item):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, item: Item): # insert an item into the bst
        self.root = self._insert(self.root, item)

    def _insert(self, node, item): # recursive helper for insert
        if node is None:
            return BSTNode(item)
        if item.id < node.item.id:
            node.left = self._insert(node.left, item)
        elif item.id > node.item.id:
            node.right = self._insert(node.right, item)
        return node

    def search(self, id: str): # search for an item by id
        return self._search(self.root, id)

    def _search(self, node, id): # recursive helper for search
        if node is None:
            return None
        if id == node.item.id:
            return node.item
        elif id < node.item.id:
            return self._search(node.left, id)
        else:
            return self._search(node.right, id)

    def inorder(self): # return items inorder
        result = []
        self._inorder(self.root, result)
        return result
        

    def _inorder(self, node, result): # recursive helper for inorder traversal
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.item)
            self._inorder(node.right, result)

    def remove(self, item: Item): # remove an item from the bst
        self.root = self._remove(self.root, item.id)

    def _remove(self, node, id): # recursive helper for remove
        if node is None:
            return node
        if id < node.item.id:
            node.left = self._remove(node.left, id)
        elif id > node.item.id:
            node.right = self._remove(node.right, id)
        else:
            # node to delete found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # node with two children: get inorder successor (smallest in right subtree)
            min_larger_node = self._min_value_node(node.right)
            node.item = min_larger_node.item
            print("DEBUG:", node.item)
            node.right = self._remove(node.right, min_larger_node.item.id)
        return node

    def _min_value_node(self, node): # helper to find the node with the smallest value
        current = node
        while current.left is not None:
            current = current.left
        return current