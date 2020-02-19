from room import Room

# Declare all the rooms


outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""")

locations = [outside, foyer, overlook, narrow, treasure]

# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

class Adventure:
    def __init__(self, adventure_name, locations = [], play = True):
        self.adventure_name = adventure_name
        self.locations = locations
        self.play = play

    def __str__(self):
        return f'\nHello, and welcome to {self.adventure_name}! \n enter "Q" at anytime to quit'

my_adventure = Adventure("The beSSt adventure GGamE", [loc for loc in locations ])

print(my_adventure)

while my_adventure.play:
    print(my_adventure.locations[user_choice])
    user_choice = input('Would you like to play? S for start, Q for quit: ')


# if start.upper() == "S":
#     print(my_adventure)
#     print(my_adventure.locations[0])
#     locChoice = input('Where would you like to go? (N, S , E , W)')

# while start.upper() == "S":
#     print(my_adventure.locations[locChoice])
#     start = input('Would you like to play? S for start, Q for quit: ')
    