"""
CECS 277 - Section 07
Professor Kate Nguyen
Group 4: 
Thanh Phat Bui
Ha Gia Bao Hoang
Description: Lab 09 - Escape room
Write a program that simulates an escape room by having the user open a series of three doors
random chosen from several different types of doors. Use the following class diagram to create
your program (you must create a main, the Door interface, and Basic Door, then you can choose
any two of the remaining four types of door to implement
"""
from basic_door import BasicDoor
from locked_door import LockedDoor
from  deadbolt_door import DeadboltDoor
from combo_door import ComboDoor
from code_door import CodeDoor
import check_input
import random


def open_door(door):
    """
    Handles the process of attempting to open a given door.

   :param door: Door
        The door object the player must unlock.
    """
    print(door.examine_door())
    while not door.is_unlocked():
        print(door.menu_option())
        input = check_input.get_int_range("> ", 1, door.get_menu_max())
        print(door.attempt(input))
        print(door.success())


def main():
    """
    Main function to run the Escape Room game.

    The player must successfully unlock 3 randomly chosen doors 
    from the available set to escape."""
    print("Welcome to Escape Room\nYou must unlock 3 doors to escape")
    # initialize an array of all doors
    escape_room = [BasicDoor(), LockedDoor(), DeadboltDoor(), ComboDoor(), CodeDoor()]
    # loop through random 3 doors
    for index in range(3):
        random_door = random.randint(0, len(escape_room) - 1)
        open_door(escape_room[random_door])
    print("Congratulation! You escaped...This time")
    
if __name__ == """__main__""":
    main()