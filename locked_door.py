from door import Door
import random
class LockedDoor(Door):
    def __init__(self):
        """
        Initializes a LockedDoor object with a hidden key.

        Attributes:
            _key_location (int): The location where the key is hidden 
                                 (randomly chosen between 1 and 3).
            _input (int): The user's last attempted location to search for the key.
        """
        self._key_location = random.randint(1,self.get_menu_max())
        self._input = 0
    def examine_door(self): 
        """
        Provides a description of the door to the user.

        :return: str
            A message describing the locked door and hinting that a key is hidden nearby.
        """
        return "You have encountered a locked door. The key is hidden nearby. Look around for the key."
    
    def menu_option(self):
        """
        Returns the available menu options for searching for the key.

        :return: str
            A formatted string showing possible places to look for the key.
        """
        return """
1. Look under the mat
2. Look under the flower pot
3. Look under the fake rock"""
    
    def get_menu_max(self): 
        """
        Provides the maximum number of menu options available.

        :return: int
            The total number of search locations (3).
        """
        return 3
    
    def attempt(self, option):
        """
        Records the user's search attempt and returns a message about the action.

        :param option: int
            The location the user chose to search (1–3).
        :return: str
            A message describing where the user looked.
        """
        self._input = option
        match option: 
            case 1: 
                return "You looked under the mat"
            case 2: 
                return "You looked under the flower pot"
            case 3: 
                return "You looked under the fake rock"
    
    def is_unlocked(self):
        """
        Checks if the door is unlocked by comparing the user's input 
        with the actual key location.

        :return: bool
            True if the user searched the correct location, False otherwise.
        """
        if(self._input == self._key_location):
            return True
        return False

    def clue(self): 
        """
        Provides a generic hint if the key has not been found yet.

        :return: str
            A message encouraging the user to search somewhere else.
        """
        return "Look somewhere else"

    def success(self):
        """
        Determines the outcome of the user's interaction with the door.

        :return: str
            A success message if the correct location was chosen,
            otherwise a clue to keep searching.
        """
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()