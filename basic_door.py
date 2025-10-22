from door import Door
import random
# The BasicDoor class represents a simple door mechanism.
# It can be unlocked by either pushing or pulling, with the correct action
class BasicDoor(Door):
    def __init__(self):
       """
        Initializes the BasicDoor object with the following attributes:
        - _state: int - Represents the correct action to unlock the door (1 for push, 2 for pull).
        - _input: int - Stores the user's input (1 for push, 2 for pull).
        """ 

       self._state = random.randint(1,self.get_menu_max())
       self._input = 0
    def examine_door(self):
        """
        Provides a description of the door.
        :return: A string describing the door as one that can be pushed or pulled.
        """
        return "You have encountered a door that is either pushed to open, or pulled"

    def menu_option(self):
        """
        Displays the menu options for interacting with the door.
        :return: A string listing the available actions (1 for Push, 2 for Pull).
        """
        return """
1. Push
2. Pull"""

    def get_menu_max(self):
        """
        Returns the maximum number of menu options available.
        :return: An integer representing the maximum menu option (2 in this case).
        """
        return 2
    
    def attempt(self, option):
        """
        Records the user's attempt to open the door and provides feedback.
        :param option: int - The user's chosen action (1 for Push, 2 for Pull).
        :return: A string describing the action taken by the user.
        """
        self._input = option
        match option:  # Matches the user's input
            case 1: 
                return "You push the door"  # Feedback for pushing the door.
            case 2: 
                return "You pull the door"  # Feedback for pulling the door.

    def is_unlocked(self):
        """
        Checks if the door is unlocked based on the user's input.
        :return: True if the user's input matches the correct action (_state), False otherwise.
        """
        if(self._input == self._state):
            return True
        return False
    def clue(self):
        """
        Provides a clue to the user if the door remains locked.
        :return: A string suggesting the user try the opposite action.
        """
        return "Try the other way"
    
    def success(self):
        """
        Determines the outcome of the user's attempt to open the door.
        :return: A success message if the door is unlocked, or a clue if it remains locked.
        """
        if(self.is_unlocked()):# Checks if the door is unlocked.
            return "Congratulation, you opened the door"
        else: 
            return self.clue() # Provides a clue if the door is still locked.

