"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item
class Inventory:
    def __init__(self):
      self._item = []
# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.


    def add_item(self, name, price, qty):
        for item in self._item:
            if item.name == name:
                print(f"Item, {item.name} already exits")
                return
            new_item = item(name, price, qty)
            self._item.append(new_item)
            print(f"item, {item.name} has been added:")
        
    def delete_item(self, name):
        item_selection = input(f"What item would you like to delete? ")
        for item in self._item:
            if item.name == item_selection:
                self._item.remove
                print(f"Item, {item_selection} has been removed:")
                return
        print(f"Item, {item_selection} is not in the list")
    def print_list(self, name, price, qty):
        for item in self._item:
            print (f"{item.name}, {item.price}, {item.qty}:")
            
    def update_item(self, name, price, qty):

        print("")








# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.
