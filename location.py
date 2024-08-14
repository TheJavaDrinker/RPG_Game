class Location:
    def __init__(self, location_name):
        self.name = location_name # Sets the name of the location (also used for characters and items)
        self.description = None # Sets the description of the location (also used for characters and items)
        self.linked_locations = {} # Empty dictionary, fills with information regarding adjacent locations
        self.character = None # Sets the character that appears in the location
        self.item = None # Sets the item that appears in the location

    def set_description(self, location_description): # Sets the description of the location
        self.description = location_description

    def get_description(self): # Returns the description of the location
        return self.description
    
    def set_name(self, location_name): # Sets the name of the location
        self.name = location_name
    
    def get_name(self): # Returns the name of the location
        return self.name
    
    def set_character(self, new_character): # Sets the character in the location
        self.character = new_character

    def get_character(self): # Returns the character in the location
        return self.character
    
    def set_item(self, new_item): # Sets the item in the location
        self.item = new_item

    def get_item(self): # Returns the item in the location
        return self.item
    
    def describe(self): # Prints the description of the location
        print(self.description)

    def link_location(self, location_to_link, direction): # Links the location to other locations with "north", "south", "east" or "west"
        self.linked_locations[direction] = location_to_link

    def get_details(self): # Prints the name and description of the location, along with the adjacent room and its direction
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_locations:
            location = self.linked_locations[direction]
            print("The " + location.get_name() + " is " + direction)

    def move(self, direction): # Allows the player to move between the rooms
        if direction in self.linked_locations: # Eg. The player moves north while in the Hideout
            return self.linked_locations[direction]
        else: # Eg. The player attempts to move west while in the hideout
            print("You can't go that way")
            return self

    def set_character(self, character): # Sets the character for that location
        self.character = character

    def get_character(self): # Returns the character for that location
        return self.character
    
    def name(self): # Prints the name of the location
        print(self.name)