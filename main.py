from item import Item
from item_manager import ItemManager

def main():
    manager = ItemManager() # create an object of item manager

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Update item")
        print("3. Delete item")
        print("4. Undo delete")
        print("5. Show all items")
        print("6. Manage item priorities")
        print("7. Search item")
        print("8. Save to file")
        print("9. Load from file")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            id = input("ID: ")
            if not id.isdigit(): # check if id is a number
                print("ID must be a number.")
                continue
            name = input("Name: ")
            category = input("Category: ")
            description = input("Description: ")
            priority = input("Priority (urgent/normal): ").lower()
            if priority not in {"urgent", "normal"} : # check if priority is invalid/empty
                print("Invalid priority defaulting to normal.")
                priority = "normal"
            item = Item(id, name, category, description, priority) # create an item object
            manager.add_item(item) # add item to manager

        elif choice == "2":
            manager.update_item()
            

        elif choice == "3":
            manager.delete_item() # delete an item

        elif choice == "4":
            manager.undo_delete() # undo the last delete operation
            

        elif choice == "5":
            manager.show_all_items() # show all items in the linked list
            

        elif choice == "6":
            manager.manage_priority_items() # manage item priorities in priority queue
            

        elif choice == "7":
            keyword = input("Enter name or category to search: ")
            results = manager.search_item(keyword) # search for items by name or category in bst
            if results:
                for item in results:
                    print(f"{item.id} - {item.name} ({item.category}, {item.priority})")
            else:
                print("No items found.")
            

        elif choice == "8":
            FILENAME = input("Enter the filename to save (without extension): ")
            manager.save_to_file(FILENAME) # save items to file
            

        elif choice == "9":
            FILENAME = input("Enter the filename to load (without extension): ")
            manager.load_from_file(FILENAME) # load items from file
            
        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid input. Try again.")


main()
