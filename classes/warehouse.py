# Define a Warehouse class to represent a warehouse
class Warehouse:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.inventory = {}
        
    def add_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
            
    def remove_inventory(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
        else:
            print("Error: Not enough inventory to fulfill order.")

# Create a warehouse at location "Houston" with a capacity of 500
warehouse = Warehouse("Houston", 500)

# Add 10 units of item "A" to the warehouse's inventory
warehouse.add_inventory("A", 10)

# Remove 5 units of item "A" from the warehouse's inventory
warehouse.remove_inventory("A", 5)