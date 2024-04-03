# Andrew Butler             10-14-2022
# Assignment #4

import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 6

# Combat function; takes in player_HP, will return modified player_HP
def combat(player_HP):
    # Random number between 0 and 2, for a 2/3 chance of combat and 1/3 of no combat.
    fight_chance = random.randrange(0,3)
    # Variables to control combat
    skeleton_HP = 2
    skeleton_AP = 2
    player_AP = 1
    hitChance = 3
    currentTurn = random.randrange(0,2)
    if fight_chance == 1 or fight_chance == 2:
        print("There is a skeleton monster in the room!")
        print("The skeleton has {0} HP and can inflict {1} damage.".format(skeleton_HP, skeleton_AP))
        # combat loop
        while player_HP > 0 and skeleton_HP > 0:
            # Player's turn
            if currentTurn == 0:
                print()
                fight_yesno = input("Do you wish to [a]ttack or [d]odge?: ")
                if fight_yesno == "a":
                    hit = random.randrange(0, hitChance)
                    if hit == 1 or hit == 2:
                        skeleton_HP -= player_AP
                        print()
                        print("You hit the skeleton! The skeleton now has {0} HP.".format(skeleton_HP))
                    elif hit == 0:
                        print()
                        print("You missed the skeleton! The skeleton still has {0} HP.".format(skeleton_HP))
                elif fight_yesno == "d":
                    # changes hitchance to force skeleton to miss
                    hitChance = 1
                else:
                    print()
                    print("Please enter [a]ttack or [d]odge...")
                    continue
            
            # Skeleton monster's turn
            if currentTurn == 1:
                hit = random.randrange(0, hitChance)
                if hit == 1 or hit == 2:
                    player_HP -= skeleton_AP
                    print()
                    print("The skeleton has hit you! You now have {0} HP.".format(player_HP))
                elif hit == 0:
                    print()
                    print("The skeleton missed! You still have {0} HP.".format(player_HP))
                hitChance = 3 # reseting hitChance if [D] was entered
            # switching turns
            currentTurn = currentTurn + 1
            currentTurn = currentTurn % 2
        # printing out fight winner, returning player_HP
        if skeleton_HP <= 0:
            print()
            print("You have defeated the skeleton monster!")
        elif player_HP <= 0:
            print()
            print("The skeleton monster has killed you!")
        else:
            print("Terrible things have happened if this message shows up")
    else:
        print("The room is devoid of life.")
    return(player_HP)

# story function; takes in room number and if that room has been previously visited; will print flavor text depending on what room and if it's been visited
def story(roomnum, visited_room):
    if roomnum == 1 and visited_room == False:
        print()
        print("You enter the dungeon, readying yourself for whatever lies inside....")
    if roomnum == 2 and visited_room == False:
        print()
        print("This room seems to a be a crossroads of sorts...")
    if roomnum == 5 and visited_room == False:
        print()
        print("You see the dungeon's exit directly ahead. You wonder if you should leave now or continue exploring...")

# Shop function; Takes in the goldAmount and player_HP, returns modified goldAmount and player_HP
def shop(goldAmount, player_HP):
    print("You come across a small clinic, with a doctor offering to heal you- for a fee, of course.")
    print("You have {0} gold pieces, and you have {1} HP.".format(goldAmount, player_HP))
    while True:
        heal_YesNo = input("Do you wish to heal for 15 gold? [y]es [n]o: ")
        if heal_YesNo == "y":
            if goldAmount >= 15:
                player_HP = 10
                goldAmount -= 15
                print("You now have {0} HP and {1} gold.".format(player_HP, goldAmount))
                break
            else:
                print()
                print("Unfortunately, you do not have enough gold. You decide to move on.")
                break
        elif heal_YesNo == "n":
            print()
            print("You decide to move on.")
            break
        else:
            print()
            print("Please enter [y] or [n].")
    return(goldAmount, player_HP)

# goldcollection function; takes in whether the room has been previously visited and the current value of goldAmount. Returns modified visited_room and goldAmount.
def goldcollection(visited_room, goldAmount):
    if visited_room == False:
        room_gold = random.randrange(10, 30, 10) # This is the amount of gold the room contains.
        print()
        print("The room has {0} gold in it.".format(room_gold))
        goldAmount += room_gold
        print("After taking the gold, you have {0} gold.".format(goldAmount))
        print()

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have visited this room before...")
        print()
    return(visited_room, goldAmount)

# movement fuction; takes imput for the current room, and what room is n, s, e, w from that room. Outputs roomChoice.
def movement(roomnum, n, s, e, w ):
    # (6 is exit)    6 6 6
    #                5 5 5
    # Rooms layout   4 2 3
    #                4 1 3
    # a bunch of if statements so that only the directions that you can go will be offered for each room.
    # for example, room 1 only has rooms to the North, East, and West of it, so the only options are n, e, and w.
    if roomnum == 1:
        direction = input("[n] [e] [w]?: ")
        while direction != "n" and direction != "e" and direction != "w":
            print("Invalid input...")
            direction = input("[n] [e] [w]?: ")
    # room 2 has rooms in every direction around it, so all options are available.
    elif roomnum == 2:
        direction = input("[n] [s] [e] [w]?: ")
        while direction != "n" and direction != "s" and direction != "e" and direction != "w":
            print("Invalid input...")
            direction = input("[n] [s] [e] [w]?: ")
    # The only options from rooms 3 and 4 are n, e, and w (see layout). Moving w or e will just wrap around; so e of room 3 is room 4.
    elif roomnum == 3 or roomnum == 4:
        direction = input("[n] [e] [w]?: ")
        while direction != "n" and direction != "e" and direction != "w":
            print("Invalid input...")
            direction = input("[n] [e] [w]?: ")
    # room only has rooms to the North and South, so only n and s are available.
    elif roomnum == 5:
        direction = input("[n] [s]?: ")
        while direction != "n" and direction != "s":
            print("Invalid input...")
            direction = input("[n] [s]?: ")
    if direction == "n":
        roomChoice = n
    elif direction == "s":
        roomChoice = s
    elif direction == "e":
        roomChoice = e
    elif direction == "w":
        roomChoice = w
    else:
        print("Terrible things have happened")
    return(roomChoice)

# Functions to represent dungeon rooms
def room1(goldAmount, visited_room, player_HP):
    story(1, visited_room)
    visited_room, goldAmount = goldcollection(visited_room, goldAmount)
    roomChoice = movement(1, 2, None, 3, 4)
    return roomChoice, goldAmount, visited_room, player_HP
    
def room2(goldAmount, visited_room, player_HP):
    story(2, visited_room)
    player_HP = combat(player_HP)
    if player_HP > 0:
        visited_room, goldAmount = goldcollection(visited_room, goldAmount)
        roomChoice = movement(2, 5, 1, 3, 4)
    else:
        roomChoice = 6
    return roomChoice, goldAmount, visited_room, player_HP

def room3(goldAmount, visited_room, player_HP):
    player_HP = combat(player_HP)
    if player_HP > 0:
        visited_room, goldAmount = goldcollection(visited_room, goldAmount)
        roomChoice = movement(3, 5, None, 4, 2)
    else:
        roomChoice = 6
    return roomChoice, goldAmount, visited_room, player_HP

def room4(goldAmount, visited_room, player_HP):
    goldAmount, player_HP = shop(goldAmount, player_HP)
    visited_room, goldAmount = goldcollection(visited_room, goldAmount)
    roomChoice = movement(4, 5, None, 2, 3)
    return roomChoice, goldAmount, visited_room, player_HP

def room5(goldAmount, visited_room, player_HP):
    story(5, visited_room)
    player_HP = combat(player_HP)
    if player_HP > 0:
        visited_room, goldAmount = goldcollection(visited_room, goldAmount)
        roomChoice = movement(5, 6, 2, None, None)
    else:
        roomChoice = 6
    return roomChoice, goldAmount, visited_room, player_HP

# Main function
def main():
    gameOver = False
    # Player status variables/ constants. 
    start_HP = 10
    START_GOLD = 0
    player_HP = start_HP
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False

    print("Welcome to Dungeon Crawl...")
    print()

    print("By: Andrew Butler")
    print("[COM S 127 B]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p":
            # main gameplay loop; goes through different room functions
            while currentRoom != FINAL_ROOM:
                if currentRoom == 1:
                    currentRoom, goldAmount, visited_room1, player_HP = room1(goldAmount, visited_room1, player_HP)
                elif currentRoom == 2:
                    currentRoom, goldAmount, visited_room2, player_HP = room2(goldAmount, visited_room2, player_HP)
                elif currentRoom == 3:
                    currentRoom, goldAmount, visited_room3, player_HP = room3(goldAmount, visited_room3, player_HP)
                elif currentRoom == 4:
                    currentRoom, goldAmount, visited_room4, player_HP = room4(goldAmount, visited_room4, player_HP)
                elif currentRoom == 5:
                    currentRoom, goldAmount, visited_room5, player_HP = room5(goldAmount, visited_room5, player_HP)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
            # message printout if player successfully escapes dungeon
            if player_HP > 0:
                print()
                print("You have escaped with", goldAmount, "gold from the dungeon!")
                print()
            # message printout if player dies in dungeon
            elif player_HP <= 0:
                print()
                print("You failed to escape the dungeon. You had {0} gold before perishing.".format(goldAmount))
                print()
            else:
                print("error; things have gone wrong")

            # Reset player values back to their original state
            goldAmount = START_GOLD
            currentRoom = START_ROOM
            player_HP = start_HP
            visited_room1 = False
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
        # intruction printout
        elif choice == "i":
            print("Fight monsters and collect gold in rooms, and decide which rooms to travel to next when prompted.")
            print("Your goal is to escape alive and with as much gold as possible- good luck!")
        # quits program
        elif choice == "q":
            print("Until next time...")
            gameOver = True
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()