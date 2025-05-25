from item import Item
from stack import Stack
from pqueue import Queue
from linkedlist import LinkedList
from bst import BST

class ItemManager:
    def __init__(self):
        self.items = LinkedList()
        self.undo_stack = Stack()
        self.priority_queue = Queue()
        self.bst = BST()  # for searching items by name and category

    def add_item(self, item: Item):
        # check if item already exists
        if self.items.getIndex(item.id) != -1:
            print(f"Item with ID {item.id} already exists.")
            return
        self.items.insert(item) # insert into linked list
        self.bst.insert(item)  # insert into BST for searching

        if item.priority == "urgent":
            self.priority_queue.items.insert(0, item)   # insert at the front for urgent items
        else:
            self.priority_queue.enqueue(item) # enqueue for normal items (end of queue)
        print(f"Item {item.name} added.")

    def update_item(self):
        if not self.items.head:
            print("No items to update.")
            return
        
        # get id from user
        print("\n--- Update Item ---")
        self.items.display()  # display all items for user to choose from
        id = input("Enter the ID of the item to update: ")
        index = self.items.getIndex(id)  # get index of item by id
        if index < 0 or index >= self.items.size():
            print("Invalid index.")
            return
        
        cur = self.items.get(index)  # get item at index from linked list
        if cur is None:
            print("No items to update.")
            return
        
        print(f"{cur}")
        # get new details from user
        name = input("Enter new name (leave blank to keep current): ")
        if not name.strip():  # if name is empty, keep current
            name = cur.name
        category = input("Enter new category (leave blank to keep current): ")
        if not category.strip():  # if category is empty, keep current
            category = cur.category
        description = input("Enter new description (leave blank to keep current): ")
        if not description.strip():  # if description is empty, keep current
            description = cur.description
        priority = input("Enter new priority (urgent/normal, leave blank to keep current): ").lower()
        if not priority.strip():  # if priority is empty, keep current
            priority = cur.priority
        elif priority not in {"urgent", "normal"}:  # check if priority is invalid
            print("Invalid priority, defaulting to normal.")
            priority = "normal"
            
        # create new item with updated details
        updated_item = Item(cur.id, name, category, description, priority)
        self.items.insert_at(index, updated_item)  # update item in linked list
        self.items.remove_at(index + 1)  # remove old item from linked list
        self.bst.remove(cur)  # remove old item from BST
        self.bst.insert(updated_item)  # insert updated item into BST
        self.priority_queue.items.remove(cur)  # remove old item from priority queue if exists
        if cur.priority == "urgent":
            self.priority_queue.items.insert(0, updated_item)
        else:
            self.priority_queue.enqueue(updated_item)

        print(f"Item {cur.name} updated to {updated_item.name}.")


    def delete_item(self):
        if not self.items.head: # check if linked list is empty
            print("No items to delete.")
            return
        
        # get id from user
        print("\n--- Delete Item ---")
        self.items.display()  # display all items for user to choose from
        id = input("Enter the ID of the item to delete: ")
        index = self.items.getIndex(id) # get index of item by id
        if index < 0 or index >= self.items.size():
            print(index)
            print("Invalid index.")
            return
        
        cur = self.items.remove_at(index) # remove item at index from linked list
        if cur is None:
            print("No items to delete.")
            return
        self.undo_stack.push((cur, index, self.priority_queue.getIndex(cur) ))  # save for undo
        self.priority_queue.items.remove(cur)  # remove from priority queue if exists
        self.bst.remove(cur)  # remove from BST

        print(f"Item {cur.name} deleted and saved for undo.")

    def undo_delete(self):
        item = self.undo_stack.pop() # pop the last deleted item from stack
        if item:
            data, index, priority = item
            self.items.insert_at(index, data)  # reinsert at the same index
            self.bst.insert(data)  # reinsert into BST for searching
            self.priority_queue.items.insert(priority, data) # reinsert into priority queue at the same index

            print("Undo successful.")
        else:
            print("Nothing to undo.")

    def search_item(self, keyword):
        # using bst to search for items by name or category
        results = []
        for item in self.bst.inorder():
            if keyword.lower() in item.name.lower() or keyword.lower() in item.category.lower():
                results.append(item) # add to results if keyword matches name or category
        return results

    def save_to_file(self, filename):
         filename = filename.strip() + ".txt"  # add .txt to file extension

         with open(filename, "w") as f: 
            items = self.items.to_list() # convert linked list to python list
            for item in items:
                # writing the item details to the file
                line = f"{item.id} - {item.name} - {item.category} - {item.description} - {item.priority}\n"
                f.write(line)
            print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        filename = filename.strip() + ".txt" # add .txt to file extension
        
        try:
            with open(filename, "r") as f:
                self.items = LinkedList()  # reset linked list
                self.undo_stack = Stack()  # reset undo stack
                self.priority_queue = Queue()  # reset priority queue
                self.bst = BST()  # reset BST for searching
                
                for line in f:
                    id, name, category, description, priority = line.strip().split("-")

                    id = int(id.strip()) # convert id to integer
                    name = name.strip() # strip whitespace from name
                    category = category.strip() # strip whitespace from category
                    description = description.strip() # strip whitespace from description
                    priority = priority.strip() # strip whitespace from priority

                    item = Item(id, name, category, description, priority)
                    self.items.insert(item)
                    self.bst.insert(item)  # insert into BST for searching
                    if item.priority == "urgent": 
                        self.priority_queue.items.insert(0, item) # insert at the front for urgent items
                    else:
                        self.priority_queue.enqueue(item) # enqueue for normal items (end of queue)
                       
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("File not found. Try again.")


    def show_all_items(self):
        if not self.items.head:
            print("No items to display.")
            return
        print("\n--- All Items --- \n")
        self.items.display()

    def manage_priority_items(self):
        if not self.priority_queue.items:
            print("No items in the priority queue.")
            return

        print("\n--- Priority Queue ---")
        counter = 1
        for item in self.priority_queue.items:
            print(f"{counter}- {item.name} ({item.priority})")
            counter += 1

        try:
            index = int(input("Select the item number you want to move: ")) - 1
            if index < 0 or index >= len(self.priority_queue.items):
                print("Invalid item number.")
                return

            print("\nMove to:")
            print("1. Top (most urgent)")
            print("2. Bottom (least urgent)")
            print("3. Custom position")

            choice = input("Your choice: ")

            item = self.priority_queue.items.pop(index)

            if choice == "1":
                self.priority_queue.items.insert(0, item)
            elif choice == "2":
                self.priority_queue.items.append(item)
            elif choice == "3":
                pos = int(input(f"Enter new position (1 to {len(self.priority_queue.items)+1}): ")) - 1
                if pos < 0 or pos > len(self.priority_queue.items):
                    print("Invalid position.")
                    self.priority_queue.items.insert(index, item)  # restore original position
                    return
                self.priority_queue.items.insert(pos, item)
            else:
                print("Invalid choice.")
                self.priority_queue.items.insert(index, item)  # restore original position
                return

            print("Item priority position updated.")

        except ValueError:
            print("Invalid input. Numbers only.")

