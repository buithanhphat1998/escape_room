from door import Door
import random
# The ComboDoor class represents a door with a combination lock.
# The door is unlocked by matching a randomly generated number (1-10) with t
class ComboDoor(Door):
    def __init__(self):
        """
        Initializes the ComboDoor object with the following attributes:
        - _correct_value: int - The randomly generated correct value to unlock the door (1-10).
        - _input_value: int - The user's input value, initialized to 0.
        """
        self._correct_value = random.randint(1,10)
        self._input_value = 0
    def examine_door(self): 
        """
        Provides a description of the door.
        :return: A string describing the door as one with a combination lock.
        """
        return "A door with a combination lock. You can spin the dial to a number 1-10"
    
    def menu_option(self):
        """
        Displays the menu option for interacting with the door.
        :return: A string prompting the user to enter a number between 1 and 10.
        """
        return "Enter # 1-10:"
    
    def get_menu_max(self) -> int: 
        """
        Returns the maximum number of menu options available for the door.
        :return: An integer representing the maximum menu option (10 in this case).
        """
        return 10
    
    def attempt(self, option):
        """
        Records the user's attempt to unlock the door by setting the input value.
        :param option: int - The user's chosen number (1-10).
        :return: A string describing the action taken by the user.
        """
        self._input_value = option
        return f"You turn the dial to...{option}"
        
    
    def is_unlocked(self):
        """
        Checks if the door is unlocked by comparing the user's input to the correct value.
        :return: True if the input matches the correct value, False otherwise.
        """
        if(self._input_value == self._correct_value):
            return True
        return False

    def clue(self): 
        """
        Provides a clue to the user if the door remains locked.
        :return: A string indicating whether the user's input is too high or too low.
        """
        if(self._input_value > self._correct_value):
            return "Too high!"
        elif(self._input_value < self._correct_value):
            return "Too low!" 

    def success(self):
        """
        Determines the outcome of the user's interaction with the door.
        :return: A success message if the door is unlocked, or a clue if it remains locked.
        """
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()