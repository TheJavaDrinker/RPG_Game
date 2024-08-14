from location import Location # Imports the Location class from location.py
from character import Enemy, Friend # Imports the Enemy and Friend class from character.py
from item import Item # Imports the Item class from item.py
from player import Player # Imports the Player class from player.py
import random # imports the random module

# Setting the location names and description

hideout = Location("Hideout") 
hideout.set_description("The place where you'll begin your journey to overthrow the overlords of this city")

noodle_shop = Location("Noodle Shop")
noodle_shop.set_description("A small, family-run shop that sells the most delicious noodles")

gymnasium = Location("Gymnasium")
gymnasium.set_description("A pristine gym, complete with state-of-the-art, 24/7 surveillance")

mayor_residence = Location("Mayor's Residence")
mayor_residence.set_description("The home of the mayor of this corrupt city, eager to do the bidding of his ruler")

slums = Location("Slums")
slums.set_description("The part of the city where the poorest of the poor reside, with no one to listen to their cries")

chinatown_SE = Location("Chinatown SE")
chinatown_SE.set_description("The south-eastern section of Chinatown, where crime and looting runs rampant. There appears to be an underground entrance here...")

chinatown_E = Location("Chinatown E")
chinatown_E.set_description("The eastern section of Chinatown, overlooking a large dam")

chinatown_NE = Location("Chinatown NE")
chinatown_NE.set_description("The north-eastern section of Chinatown, where the police perform regular patrols of the area for dissidents")

chinatown_N = Location("Chinatown N")
chinatown_N.set_description("The northern section of Chinatown, filled with various stores and gadgets")

mega_market = Location("Mega Market")
mega_market.set_description("A massive supermarket, filled with various low-quality produce and foodstuffs")

police_precinct = Location("Police Precinct")
police_precinct.set_description("Home of the city's police department, who will only respond to the worst crimes - those against the state")

tenkaichi_alley = Location("Tenkaichi Alley")
tenkaichi_alley.set_description("One of the city's major alleyways, where violence is commonplace")

tenkaichi_alley_N = Location("Tenkaichi Alley North")
tenkaichi_alley_N.set_description("The northern section of Tenkaichi Alley - not as dangerous as the rest of the alley")

homeless_den = Location("Homeless Den")
homeless_den.set_description("The major homeless section of the city, where the condemned are left to be forgotten. There appears to be an underground entrance here...")

bait_and_tackle = Location("Bait and Tackle Shop")
bait_and_tackle.set_description("A humble store where people can purchase gear for their fishing adventures")

pier = Location("Pier")
pier.set_description("A expansive pier, though the water is too murky to see any fish")

national_road_W = Location("National Road West")
national_road_W.set_description("The western section of National Road, where national gaurds perform routine patrols")

national_road = Location("National Road")
national_road.set_description("The major road of the city, where the government's headquarters are located")

national_road_E = Location("National Road East")
national_road_E.set_description("The eastern section of National Road, where supplies are being delivered by the hour")

ski_slope_low_entrance = Location("Ski Slope Low Entrance")
ski_slope_low_entrance.set_description("The lower entrance of the ski slope, where people are waiting eagerly to board")

ski_slope_high_entrance = Location("Ski Slope High Entrance")
ski_slope_high_entrance.set_description("The higher entrance of the ski slope, overlooking the city and the highway")

snow_covered_cave_entrance = Location("Snow-covered Cave Entrance")
snow_covered_cave_entrance.set_description("An entrance to a cave covered by a thick layer of snow. There appears to be a light emanating from within the cave...")

cavern = Location("Cavern")
cavern.set_description("A dark and damp cave, with the sound of insects crawling being heard")

campfire = Location("Campfire")
campfire.set_description("A dim campfire that is barely burning, with a pot hanging above the flames")

cavern_shop = Location("Cavern Shop")
cavern_shop.set_description("A small, wooden storefront run by an elderly escaped 'convict'")

grassy_knolls = Location("Grassy Knolls")
grassy_knolls.set_description("A set of small hills, accompanied with large patches of dead grass")

wooden_bridge_N = Location("Wooden Bridge North")
wooden_bridge_N.set_description("The northern end of a wooden rickety bridge overhanging a large body of water")

wooden_bridge_S = Location("Wooden Bridge South")
wooden_bridge_S.set_description("The southern end of a wooden rickety bridge overhanging a large body of water")

ancient_monument = Location("Ancient Monument")
ancient_monument.set_description("A ancient piece of history, reminding us of a bygone era")

national_highway = Location("National Highway")
national_highway.set_description("The entrance to the major highway of the city, guarded by CCTV and multiple checkpoints")

service_station = Location("Service Station")
service_station.set_description("A decrepit service station in the middle of nowhere")

mcburger_town = Location("McBurger Town")
mcburger_town.set_description("A fast food joint, run by the government to keep track of their citizen's health")

highway_exit = Location("Highway Exit Ramp")
highway_exit.set_description("The exit ramp for the National Highway, also guarded by patrols - you'll need to find an alternative exit")

abandoned_train_depot = Location("Abandonded Train Depot")
abandoned_train_depot.set_description("An abandoned train depot, with various trains from different eras no longer used. You can see a shaodwy figure in the distance...")

unknown = Location("???")
unknown.set_description("Where are you? What is this place? Where has the figure gone?")

# Linking the locations together

hideout.link_location(noodle_shop, "east")
hideout.link_location(national_road_E, "north")

noodle_shop.link_location(chinatown_N, "east")
noodle_shop.link_location(gymnasium, "south")

gymnasium.link_location(noodle_shop, "north")
gymnasium.link_location(mayor_residence, "south")

mayor_residence.link_location(gymnasium, "north")
mayor_residence.link_location(slums, "east")
mayor_residence.link_location(mega_market, "south")

slums.link_location(mayor_residence, "west")
slums.link_location(chinatown_SE, "east")

chinatown_SE.link_location(chinatown_E, "north")
chinatown_SE.link_location(homeless_den, "east")
chinatown_SE.link_location(slums, "west")

chinatown_E.link_location(chinatown_SE, "south")
chinatown_E.link_location(chinatown_NE, "north")

chinatown_NE.link_location(chinatown_E, "south")
chinatown_NE.link_location(chinatown_N, "west")

chinatown_N.link_location(noodle_shop, "west")
chinatown_N.link_location(chinatown_NE, "east")

mega_market.link_location(mayor_residence, "north")
mega_market.link_location(police_precinct, "west")

police_precinct.link_location(mega_market, "east")
police_precinct.link_location(tenkaichi_alley, "west")

tenkaichi_alley.link_location(police_precinct, "east")
tenkaichi_alley.link_location(tenkaichi_alley_N, "north")

tenkaichi_alley_N.link_location(tenkaichi_alley, "south")
tenkaichi_alley_N.link_location(homeless_den, "west")

homeless_den.link_location(tenkaichi_alley_N, "east")
homeless_den.link_location(chinatown_SE, "west")
homeless_den.link_location(bait_and_tackle, "north")

bait_and_tackle.link_location(homeless_den, "south")
bait_and_tackle.link_location(pier, "west")
bait_and_tackle.link_location(national_road_W, "north")

pier.link_location(bait_and_tackle, "east")

national_road_W.link_location(bait_and_tackle, "south")
national_road_W.link_location(national_road, "east")

national_road.link_location(national_road_W, "west")
national_road.link_location(national_road_E, "east")

national_road_E.link_location(national_road, "west")
national_road_E.link_location(hideout, "south")
national_road_E.link_location(ski_slope_low_entrance, "north")

ski_slope_low_entrance.link_location(ski_slope_high_entrance, "north")
ski_slope_low_entrance.link_location(national_road_E, "south")
ski_slope_low_entrance.link_location(grassy_knolls, "east")

ski_slope_high_entrance.link_location(ski_slope_low_entrance, "south")
ski_slope_high_entrance.link_location(snow_covered_cave_entrance, "west")

snow_covered_cave_entrance.link_location(ski_slope_high_entrance, "east")
snow_covered_cave_entrance.link_location(cavern, "north")

cavern.link_location(snow_covered_cave_entrance, "south")
cavern.link_location(campfire, "west")
cavern.link_location(cavern_shop, "north")

campfire.link_location(cavern, "east")

cavern_shop.link_location(cavern, "south")

grassy_knolls.link_location(ski_slope_low_entrance, "west")
grassy_knolls.link_location(wooden_bridge_N, "east")

wooden_bridge_N.link_location(grassy_knolls, "west")
wooden_bridge_N.link_location(wooden_bridge_S, "south")

wooden_bridge_S.link_location(wooden_bridge_N, "north")
wooden_bridge_S.link_location(ancient_monument, "east")

ancient_monument.link_location(wooden_bridge_S, "west")
ancient_monument.link_location(national_highway, "east")

national_highway.link_location(ancient_monument, "west")
national_highway.link_location(service_station, "north")

service_station.link_location(national_highway, "south")
service_station.link_location(mcburger_town, "north")

mcburger_town.link_location(service_station, "south")
mcburger_town.link_location(highway_exit, "north")

highway_exit.link_location(mcburger_town, "south")
highway_exit.link_location(abandoned_train_depot, "west")

abandoned_train_depot.link_location(highway_exit, "east")
abandoned_train_depot.link_location(unknown, "north")

unknown.link_location(abandoned_train_depot, "south")

# Setting enemy names, conversations, weaknesses and location

robocop = Enemy("RoboCop", "One of the governments newly developed robotic police officers, made to maintain 'law and order'", "Nothing", False)
robocop.set_conversation("YOU ARE OUT PAST THE STATE-MANDATED CURFEW CITIZEN. RETURN TO YOUR RESIDENCE IMMEDIATELY.")
robocop.set_weakness("stun gun")
chinatown_SE.set_character(robocop)

juggernaut = Enemy("Juggernaut", "A heavily armoured combatant, built to withstand the toughest threats", "Cocky", False)
juggernaut.set_conversation("What are you doing here, citizen? There's no fish here, anyways.")
juggernaut.set_weakness("energy blade")
pier.set_character(juggernaut)

patrol = Enemy("Military Patrol", "A large group of military roamers, you'll have to target them all at once", "Protected", False)
patrol.set_conversation("Keep on moving citizen, there's nothing out here for you to see.")
patrol.set_weakness("hand grenade")
grassy_knolls.set_character(patrol)

sniper = Enemy("Sniper", "A long range sniper unit, you'll have to find a way to attack him from a distance", "Focused", False)
sniper.set_conversation("[You are too far away to talk to the sniper]")
sniper.set_weakness("M82 rifle")
abandoned_train_depot.set_character(sniper)

general = Enemy("General Townsend", "The military leader of the country, ascending to power in 2070 after overthrowing the president", "Scornful", False)
general.set_conversation("End of the line for you and your rebellion, boy.")
general.set_weakness("MG42 machinegun")
national_road.set_character(general)

barrier = Enemy("National Highway Barrier", "The fiercest enemy you will ever face on your journey... a toll booth.", "...Blocky", False)
barrier.set_conversation("[It's... a toll booth, it can't speak.]")
national_highway.set_character(barrier)

# Setting item names, descriptions and locations

stun = Item("stun gun", "★☆☆☆☆ - Common" )
stun.set_description("A stun gun capable of delivering an electric shock of 30,000 volts")
homeless_den.set_item(stun)

blade = Item("energy blade", "★☆☆☆☆ - Common")
blade.set_description("The sharpest blade, crafted with energy of the highest order and armor-piercing capabilities")
hideout.set_item(blade)

grenade = Item("hand grenade", "★☆☆☆☆ - Common")
grenade.set_description("A simple hand grenade, with a range of around 10 metres. Good for fighting multiple opponents")
service_station.set_item(grenade)

rifle = Item("M82 rifle", "★★☆☆☆ - Uncommon")
rifle.set_description("A long-distance sniper rifle, capable of taking out a target at around 2 kilometres and equipped with a target finder.")
cavern_shop.set_item(rifle)

medication = Item("MedPack", "★★★★☆ - Epic") # This item is used on the player, not on an enemy
medication.set_description("A medical dispenser that injects morphine, giving you an extra boost.")
tenkaichi_alley.set_item(medication)

machinegun = Item("MG42 machinegun", "★★★★★ - Legendary")
machinegun.set_description("A relic of an old era, a WWII machinegun capable of firing 1500 rounds per minute")
unknown.set_item(machinegun)

tokens = Item("tokens", "★★★☆☆ - Rare")
tokens.set_description("A bundle of 1000 tokens, the new currency of the city.")
chinatown_NE.set_item(tokens)

# Setting friendly NPC names, descriptions, conversations and locations

franklin = Friend("Franklin", "The eldery owner of the rickety shop in the cavern.", "Scared", False)
franklin.set_conversation("I miss the old days when the government didn't have eyes on you 24/7.")
cavern_shop.set_character(franklin)

joseph = Friend("Joseph", "Another refugee from when the military took control of the city.", "Tired", False)
joseph.set_conversation("I hear that you might be able to find some weapons near the abandoned train depot.")
campfire.set_character(joseph)

robert = Friend("Robert", "The owner of the bait and tackle shop near the pier.", "Disheartened", False)
robert.set_conversation("Don't bother buying anything, there isn't anything in the pier to catch anyways.")
bait_and_tackle.set_character(robert)

johnson = Friend("Johnson", "An old friend of mine that was drafted into the police force to serve the military.", "Stern", False)
johnson.set_conversation("[He doesn't say anything, but passes you a note that reads: 'There's a shortcut around this area to avoid the police']")
police_precinct.set_character(johnson)

mayor = Friend("Mayor Roosevelt", "The man who used to have control over the city, but has since become powerless.", "Cheery", False)
mayor.set_conversation("Have a good night, citizen! Stay out of trouble!")
mayor_residence.set_character(mayor)

charles = Friend("Charles", "A regular of the Chinatown shops. He appears to be uneasy...", "Fearful", False)
charles.set_conversation("Stay away from the homeless den, man! They're armed to the teeth!")
chinatown_NE.set_character(charles)

raymond = Friend("Raymond", "A fellow freedom fighter watching over those who have seeked refuge in the hideout.", "Hopeful", False)
raymond.set_conversation("We believe in you, take down General Townsend and his army!")
hideout.set_character(raymond)

mary = Friend("Mary", "A citizen also gazing upon the ancient monument.", "Saddened", False)
mary.set_conversation("To think we took liberty for granted...")
ancient_monument.set_character(mary)

jenny = Friend("Jenny", "A worker at the McBurger Town on the National Highway.", "Bored", False)
jenny.set_conversation("Have you ever been up to the mountains? I hear that some refugees live up there.")
mcburger_town.set_character(jenny)

anonymous = Friend("???", "A figure that appears to have a disembodied voice.", "Powerful", False)
anonymous.set_conversation("Use this to successfully take down the overlords. Do not question its origins.")
unknown.set_character(anonymous)

player = Player(3, 0, 0, 0, 0, 0) # Initialises the player class with lives, steps, score, peaceful takedowns and kills

bag = [] # Initialises the array for the player's inventory
lives = 3 # Sets the player's health to 3 lives
steps = 0 # Sets the amount of steps taken to 0
peaceful = 0 # Sets the amount of peaceful surrenders to 0
kills = 0 # Sets the amount of kills to 0
conversations = 0 # Sets the amount of conversations to 0

current_location = hideout # Sets the starting position of the player to the hideout
dead = False # Sets the value of the dead variable to False, allowing the game to run while the player is alive

difficulty = input("Would you like to activate hardcore mode? Enemies will kill you in one shot, but you will receive greater rewards. (Y for yes, any other input for no) ")
if difficulty.upper() == "Y":
    difficulty = "hardcore"
    print("You have chosen to play on Hardcore difficulty. Good luck, you're going to need it...")
else:
    difficulty = "normal"
    print("You have chosen to play on Normal difficulty. Good luck out there, adventurer...")

while dead == False: # While the player is still alive        
    print("\n") # Prints a new line of text         
    current_location.get_details() # Retrieves the name, description and adjacent locations of the current room
    inhabitant = current_location.get_character() # Checks if there is an inhabitant in the current location
    if inhabitant is not None: # Section of code is only triggered if there is a character in the location
        inhabitant.describe() # Prints the name and description of the inhabitant
    item = current_location.get_item() # Checks if there is an item in the current location
    if item is not None: # Section of code is only triggered if there is an item in the location
        item.describe() # Prints the name and description of the item
    command = input("> ") # Allows the player to input a command

    if command in ["north", "south", "east", "west"]: # Checks to see if the player has attempted to move
        if current_location == national_highway and command == "north" and inhabitant is not None: # Checks if the player is attempting to move north while at the National Highway and the barrier is still present
            if "tokens" in bag: # Checks if the player has the currency in their bag
                bag.remove("tokens") # Removes the tokens from the players inventory
                national_highway.set_character(None) # Removes the barrier from the location
                Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1 # Reduces the amount of enemies by 1
                print("You insert the tokens into the coin slot, opening the boom gate. However, it jams shut, granting you permanent access ahead.")
                current_location = current_location.move(command) # Moves forward as expected
            else:
                print("BLOCKED BY TOLL BOOTH - PAY 1000 TOKENS TO PASS THROUGH") # Prevents player from moving forward
        else:
            current_location = current_location.move(command) # Updates current_location to be the result of the move function, with the variable command 
            player.movement(steps) # Activates the movement function for the player object, with the variable steps

    elif command == "talk": 
        if inhabitant is not None: # Checks if there is a character in the location
            inhabitant.talk() # Prints out the character's dialogue
            if inhabitant.talked_to == False:
                inhabitant.set_talked_to(True)
                player.add_conversation(conversations)


    elif command == "fight":
        if inhabitant == barrier:
            print("You attempt to punch the barrier, but you simply injure your hand in the process.")
        else:
            if inhabitant is not None and isinstance(inhabitant, Enemy): # Checks if there is an enemy character in the current location

                print("What will you fight with?")
                fight_with = input()
                if fight_with in bag: # Checks if the inputted weapon is in the player's inventory
                    if inhabitant.fight(fight_with) == True: # Check if the inputted weapon is the enemy's weakness
                        player.add_kill(kills) # Increases kill count by one
                        print("Target down, good execution.")
                        if Enemy.enemies_to_defeat == 0: # If no more enemies are left in the game.
                            print("The overlords have been truly defeated now, all thanks to your heroic efforts.") 
                            player.final_score(steps, lives, peaceful, kills, difficulty, conversations) # Prints out final score
                            player.rank(kills, difficulty) # Prints out ending
                            dead = True # Ends the game
                        current_location.set_character(None) # Removes the character from the roo
                    else:
                        player.damage(lives, difficulty) # Reduces the player's lives by 1
                        if player.lives == 0:
                            print("You have been terminated.")
                            print("The overlords will never relinquish their hold of this country...")
                            dead = True # Ends the game
                else: # If the player inputs an item that is not in their bag
                    print("You don't have a " + fight_with)

            elif isinstance(inhabitant, Friend): # If the player attempts to fight a friend.
                print(f"{inhabitant.name} doesn't want to fight you.")

            else:
                print("There is no one here to fight with")

    elif command == "greet":
        if inhabitant == barrier:
            print("Are you... trying to talk to an inanimate barrier?")
        else:
            if inhabitant is not None: # If there is a character in the location.
                if isinstance(inhabitant, Enemy): # If the character type is an enemy.
                    print("They don't exactly seem to be the friendly type...")
                else:
                    inhabitant.greet()
            else:
                print("There is no one here to greet :(")

    elif command == "take":
        if item is not None: # Checks if there is an item in the location
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name()) # Updates the bag array to include the picked up item
            if item == medication: # The MedPack in Tenkaichi Alley
                player.heal(lives, bag) # Immediately uses the item
            current_location.set_item(None) # Removes the item from the location.
        else:
            print("There is no item to take.")

    elif command == "check":
        print(f"The following items are in your bag: {bag}") # Prints the contents of the player's inventory

    elif command == "spare":
        if inhabitant == barrier:
            print("I don't think the barrier needs to be spared...")
        else:
            if inhabitant is not None and isinstance(inhabitant, Enemy): # Checks if there is an inhabitant and if they are an enemy
                number = random.randint(1, 5) # Generates a random integer from 1 to 5
                if inhabitant.spare(number) == True: # If the number is equal to 5
                        player.add_surrender(peaceful) # Increases the peaceful surrender count by 1
                        print("Good job managing to take them down peacefully.")
                        if Enemy.enemies_to_defeat == 0: # If there are no more enemies to defeat
                            print("The overlords have been truly defeated now, all thanks to your heroic efforts.")
                            player.final_score(steps, lives, peaceful, kills, difficulty) # Prints the player's final score
                            player.rank(kills, difficulty) # Prints out ending
                            dead = True # Ends the game
                        current_location.set_character(None) # Removes the character from the location
                else:
                    player.damage(lives, difficulty) # Reduces the player's lives by 1
                    if player.lives == 0: 
                        print("You have been terminated.")
                        print("The overlords will never relinquish their hold of this country...")
                        dead = True # Ends the game
            elif isinstance(inhabitant, Friend): # If the player attempts to spare a friend
                print(f"{inhabitant.name} doesn't need to be spared.")
            else:
                print("There is no one to spare.")

    else: # If the player did not input a valid command
        print("Invalid command.")