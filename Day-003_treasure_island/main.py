# Print ACSII art for winning choices
you_win = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|________
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

road_fork = input("You come to a fork in the road.  Go left or right? ")

# If user picks left, they are still alive - on to the next question.
if road_fork.lower() == "left":
    boat_swim = input("\nAfter a short distance, you reach the shore.  There's a pier and a boat coming in that can "
                      "take you a nearby archipelago.  Do you want to wait or swim? ")
    # If the user wais, they are still alive - on to the final question.
    if boat_swim.lower() == "wait":
        print("\nAfter a short boat ride with a somewhat grim-looking ferryman, you arrive.  As you get out of the "
              "boat he points to a light in the distance before rowing off.")
        print("A winding road brings you to an ancient building with three doors, each emblazoned with a time-worn "
              "rune of a different color.")
        # Pick a door.
        which_door = input("Do you open the red, yellow or blue door? ")
        # Fireball!
        if which_door.lower() == "red":
            print("A huge fireball reduces you to ash.  Perhaps it would have been wise to look at the charred tree "
                  "behind you before choosing the red door.  Game Over!")
        # Grue!
        elif which_door.lower() == "blue":
            print("The door closes behind you.  It is dark and you get eaten by a Grue.  Perhaps it would have been "
                  "wise to notice the bone fragments before choosing the blue door.  Game Over!")
        # Winner, winner - chicken dinner!
        elif which_door.lower() == "yellow":
            print("You go through the door to puppies, cookies, online banking and a treasure chest.  You Win!")
            print(you_win)
        # Invalid choice - you lose!
        else:
            print("You have made an invalid choice.  A trebuchet appears and flings you to Antarctica, where you "
                  "freeze to death.  Game Over!")
    # If user picks swim or anything else it's game over.
    else:
        print("You were dragged down to Davey Jones' locker by a Kraken.  Game Over!")
# If user picks right or anything else it's game over.
else:
    print("You stepped on a teleportation pad and ended up on a planet lacking a breathable atmosphere.  Game Over!")
