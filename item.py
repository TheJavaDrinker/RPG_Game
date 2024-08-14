class Item():
    def __init__(self, item_name, rarity): 
        self.name = item_name # Initialises the name of the item (also used for characters and locations)
        self.itemdescription = None # Initialises the description of the item
        self.rarity = rarity # Initialises the rarity of the item

    def set_name(self, item_name): # Sets the name of the item
        self.name = item_name

    def get_name(self): # Returns the name of the item
        return self.name
    
    def set_description(self, item_description): # Sets the description of the item
        self.description = item_description

    def get_description(self): # Returns the description of the item
        return self.description
    
    def get_rarity(self, rarity): # Sets the rarity of the item
        self.rarity = rarity 

    def get_rarity(self): # Returns the rarity of the item.
        return self.rarity
    
    def describe(self): # Prints the name, description and rarity of the item
        print("The [" + self.name + '] is here - ' + self.description)
        print("This item is rated: " + self.rarity)
