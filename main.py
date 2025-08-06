import json
from pathlib import Path

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
    return visitArray

def inspect():
    # Write the function to look around the room
    pass

def ask_person():
    # Write function for asking the person
    pass

def open_Door():
    pass

def start_game():
    game_info = getGameData()
    print(game_info["start_description"])
    running = True
    count = 0
    visitors =generateVisitor()
    while running:
        cm = input("Enter command: ")
        count += 1

        #input


def main():
    start_game()

if __name__ =='__main__':
    main()