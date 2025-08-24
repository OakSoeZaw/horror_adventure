import json
import sys
from pathlib import Path
import random

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
    Visitor(visitors[key]['name'],visitors[key]['type'],visitors[key]['ans'],visitors[key]['note'],False)
        for key in visitors
    ]
    random.shuffle(visitArray)
    return visitArray

def inspect(gameInfo,visitor):
    infoWhere = input("Enter Item:")
    roomInfo = gameInfo["Room"]
    if infoWhere == "room":
        print("In the room,there are:")
        for obj in roomInfo["LivingRoom"].values():
            print(obj["Description"])
    if infoWhere in roomInfo["LivingRoom"]:
        print("You inspected ", infoWhere)
        print(roomInfo["LivingRoom"][infoWhere]['inspected'])
    if infoWhere == 'note':
        print(visitor.get_note())

def ask_person(visitor):
    # Write function for asking the person
    print(f'{visitor.name} said : {visitor.Ans}')
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


def start_game():
    game_info = getGameData()
    print(game_info["start_description"])
    running = True
    count = 0
    visitors = generateVisitor()
    commands = ['open','close','inspect','help','ask','quit']
    while running:
        visitor = visitors[count]
        if not visitor.introState:
            print(f"{visitor.name} said: Hello I am here")
            visitor.introState = True
        cm = input("Enter command: ")
        print("----------------------------")
        if cm == "open":
            count = open_Door(visitor,count)
        if cm == "close":
            count = close_Door(visitor,count)
        if cm == "inspect":
            inspect(game_info,visitor)
        if cm == "help":
            print("The available commands are: ")
            for com in commands:
                print(com)
        if cm == "ask":
            ask_person(visitor)
        if cm == 'quit':
            print("Thank you for playing!")
            sys.exit()



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