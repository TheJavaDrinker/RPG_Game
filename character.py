class Character:
    def __init__(self, char_name, char_description, feeling, talked_to):
        self.name = char_name # Initialises the character's name (also used for items and locations)
        self.description = char_description # Initialises the character description (also used for locations)
        self.conversation = None # Initialises what the character will say
        self.feeling = feeling # Sets the characters mood
        self.talked_to = talked_to

    def describe(self): # Called whenever the player enters a room with a character
        print(self.name + " is here!") # Prints the character's name
        print(self.description) # Prints the character's description
        print(f"They are feeling: [{self.feeling}]")

    def set_conversation(self, conversation): # Sets what the character will say
        self.conversation = conversation

    def talk(self): # Called whenever the player uses the talk command
        if self.conversation is not None: # Checks if a character is in the location
            print("[" + self.name + " says]: " + self.conversation) # Prints the character's name, followed by their conversation
        else: # If there is no character in the location
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item): # If the player uses the fight command (default function)
        print(self.name + " doesn't want to fight with you")
        return True
    
    def spare(self, number): # If the player uses the spare command (default function)
        print(self.name + " doesn't need to be spared" )

    def set_feeling(self, feeling):
        self.feeling = feeling

    def get_feeling(self):
        return self.feeling
    
    def set_talked_to(self, talked_to):
        self.talked_to = talked_to

    def get_talked_to(self):
        return self.talked_to
    
class Enemy(Character):
    enemies_to_defeat = 0  # Sets how many enemies the player needs to defeat
    def __init__(self, char_name, char_description, feeling, talked_to): 
        super().__init__(char_name, char_description, feeling, talked_to) # Superclass of the Character class
        self.weakness = None # Initialises the enemy's weakness
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1 # Initialises how many enemies the player needs to defeat

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness # Sets the enemy's weakness

    def get_weakness(self): # Returns the enemy's weakness
        return self.weakness
    
    def set_feeling(self, feeling):
        self.feeling = feeling

    def get_feeling(self):
        return self.feeling
    
    def fight(self, combat_item): # Called when the player attempts to fight an enemy
        if combat_item == self.weakness: # Successful attack
            print("You attack " + self.name + " with the " + combat_item)
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1 # Reduces the enemies needed to be killed by 1
            return True
        else: # Unsuccessful attack
            print(self.name + "does not seem to be affected by this...")
            print(self.name + " shoots you, taking damage")
            return False
        
    def spare(self, number): # When the player attempts to spare an enemy
        if number == 5: # Successful plea
            print(self.name + " has decided to voluntarily surrender.")
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1 # Reduces the enemies that need to be defeated by 1
            return True
        else: # Unsuccessful plea
            print(self.name + " rejects your plea.")
            print(self.name + " shoots you, taking damage.")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description, feeling, talked_to):
        super().__init__(char_name, char_description, feeling, talked_to) # Superclass of the character class
        self.feeling = feeling
        self.talked_to = talked_to

    def greet(self): # When the player uses the greet command on a friend
        print(self.name + " greets you back!")