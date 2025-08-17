import json
import sys
from pathlib import Path
import random

from game import monster
from game.monster import Visitor


# need introduction for the situation you are in.

def getGameData():
    data_path = Path(__file__).parent / "data" / "game_data.json"

    with data_path.open('r') as f:
        game_data = json.load(f)
    return game_data

def generateVisitor():
    data = getGameData()
    visitors = data['visitors']
    visitArray = [
    Visitor(visitors[key]['name'],visitors[key]['type'],visitors[key]['ans'])
        for key in visitors
    ]
    random.shuffle(visitArray)
    return visitArray

def inspect():
    # Write the function to look around the room
    pass

def ask_person():
    # Write function for asking the person
    pass

def open_Door(visitor,count):
    if visitor.type == "monster":
        print("Game Over, you let a monster in.")
        sys.exit()
    else:
        print(f"{visitor.name} did the business and left")
        count += 1
    return count

def close_Door(visitor,count):
    print("You asked the person to leave")
    if visitor.type == "monster":
        print(f"{visitor.name} said 'I will get you next timeeeee'")
    else:
        print("Okay, I am going to tell your mom ")

    count +=1
    return count

def inventory():
    #write a loop for displaying all the items in the inventory
    pass

def start_game():
    game_info = getGameData()
    print(game_info["start_description"])
    running = True
    count = 0
    visitors = generateVisitor()
    inventory = []
    removedItems = set()
    while running:
        visitor = visitors[count]
        cm = input("Enter command: ")
        if cm == "open":
            count = open_Door(visitor,count)
        if cm == "close":
            count = close_Door(visitor,count)

        if count >= len(visitors):
            print("No more visitors are coming")
            while True:
                choice = input("Do you want to play again? (yes/no)")
                if choice == 'yes':
                    count = 0
                    visitors = generateVisitor()
                    print("Make sure to survive")
                    break
                else:
                    print("Thanks for playing")
                    running = False
                    break

        #input


def main():
    start_game()

if __name__ =='__main__':
    main()