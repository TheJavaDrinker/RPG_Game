class Player:
    def __init__(self, lives, score, steps, peaceful, kills, conversations):
        self.score = score # Initialises the player's score
        self.lives = lives # Initialises the player's health
        self.steps = steps # Initialises the amount of steps taken
        self.peaceful = peaceful # Initialises the amount of peaceful takedowns
        self.kills = kills # Initialises the amount of kills
        self.conversations = conversations # Initialises the amount of conversations.

    def set_score(self, score): # Sets the player's score
        self.score = score

    def get_score(self): # Returns the player's score
        return self.score
    
    def set_lives(self, lives): # Sets the player's health
        self.lives = lives

    def get_lives(self): # Returns the player's health
        return self.lives
    
    def set_conversations(self, conversations): # Sets the amount of unique conversations the player has held
        self.conversations = conversations

    def get_conversations(self): # Returns the amount of unique conversations the player has held
        return self.conversations
    
    def damage(self, lives, difficulty): # If the player uses the wrong item or an enemy, or the spare fails
        if difficulty == "hardcore":
            self.lives = 0
        else:
            self.lives -= 1 # Reduces the player's health by 1
            print(f"You only have {self.lives} lives remaining now.") # Prints how many lives are left

    def heal(self, lives, bag): # When the player interacts with the MedPack in Tenkaichi Alley
        self.lives += 5 # Increases the player's health by 5
        print(f"You feel the medication coursing through your veins. You now have {self.lives} lives left.") # Prints how many lives are left
        bag.remove("MedPack") # Removes the MedPack from the player's bag, as well as the game
        return bag # Returns the updated contents of the bag

    def movement(self, steps): # Called anytime the player moves into a room
        self.steps += 1 # Adds 1 to the player's step count

    def add_surrender(self, peaceful): # Called anytime the player successfully convinces an enemy to surrender
        self.peaceful += 1 # Adds 1 to the player's peaceful takedown count

    def add_kill(self, kills): # Called anytime the player kills an enemy
        self.kills += 1 # Adds 1 to the player's kill count

    def add_conversation(self, conversations):
        self.conversations += 1

    def final_score(self, steps, lives, peaceful, kills, difficulty, conversations): # Called if the player successfully kills/takes down all enemies
        if difficulty == "hardcore":
            self.score = ((250 - (2 * steps)) + (150 * lives) + (1000 * peaceful) + (50 * conversations)) * 10000 # Determines the player score
            print("YOU BEAT THE HARDCORE MODE! GREAT JOB!")
            print(f"Your final score is: [{self.score}]") # Prints the score
            print(f"You took {self.steps} steps") # Prints out how many steps were taken
            print(f"You took down {self.peaceful} enemies peacefully.") # Prints out how many enemies were taken down peacefully
            print(f"You killed {self.kills} enemies.") # Prints out how enemies were killed
            print(f"You talked to {self.conversations} NPCs.")
        else:
            self.score = ((250 - (2 * steps)) + (150 * lives) + (1000 * peaceful) + (50 * conversations))
            print(f"Your final score is: [{self.score}]")
            print(f"You took {self.steps} steps")
            print(f"You took down {self.peaceful} enemies peacefully.")
            print(f"You killed {self.kills} enemies.")
            print(f"You talked to {self.conversations} NPCs.")


    def rank(self, kills, difficulty): # Prints out what ending was achieved based on the amount of enemies killed
        if difficulty == "hardcore":
            if self.kills == 0:
                print("You achieved the Hardcore Pacifist ending!")
            elif self.kills > 0 and self.kills <= 2:
                print("You achieved the Hardcore Lawful Neutral ending!")
            elif self.kills > 2 and self.kills <= 4:
                print("You achieved the Hardcore Chaotic Neutral ending!")
            else:
                print("You achieved the Hardcore Genocide ending!")
        else:
            if self.kills == 0:
                print("You achieved the Pacifist ending!")
            elif self.kills > 0 and self.kills <= 2:
                print("You achieved the Lawful Neutral ending!")
            elif self.kills > 2 and self.kills <= 4:
                print("You achieved the Chaotic Neutral ending!")
            else:
                print("You achieved the Genocide ending!")