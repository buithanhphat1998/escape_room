from door import Door
import random
class DeadboltDoor(Door):
    def __init__(self):
        """
        Initializes a DeadboltDoor object with two bolts.

        Attributes:
            _bolt1 (int): Represents the first bolt (1 = locked, 0 = unlocked).
            _bolt2 (int): Represents the second bolt (1 = locked, 0 = unlocked).
        """
        # random bolt 1 from 0 to 1
        self._bolt1 = random.randint(0, 1)
        # if bolt1 is already unlock, then the second one should not be unlocked
        if(self._bolt1 == 0):
            self._bolt2 = 1
        # otherwise, randomly choose bolt2
        else:
            self._bolt2 = random.randint(0, 1)
    
    def examine_door(self): 
        """
        Returns the available menu options for interacting with the door.

        :return: str
            A formatted string displaying the available actions (toggle bolts).
        """
        return "You have encountered a door with two deadbolts. Both need to be unlocked to open the door, but you can't tell if each one is locked or unlocked."
    
    def menu_option(self):
        return  """
1. Toggle bolt 1
2. Toggle bolt 2"""
    
    def get_menu_max(self): 
        """
        Provides the maximum menu option number.

        :return: int
            The number of available options (2).
        """
        return 2
    
    def attempt(self, option):
        """
        Attempts to toggle one of the bolts based on the user's choice.

        :param option: int
            The option selected by the user (1 for bolt1, 2 for bolt2).
        :return: str
            A message describing the action taken.
        """
        match option:
            case 1: 
                if(self._bolt1 == 1):
                    self._bolt1 = 0
                else:
                    self._bolt1 = 1
                return "You toggled the first bolt"
            case 2: 
                if(self._bolt2 == 1):
                    self._bolt2 = 0
                else:
                    self._bolt2 = 1
                return "You toggled the second bolt"

    def is_unlocked(self):
        """
        Checks whether the door is completely unlocked.

        :return: bool
            True if both bolts are unlocked, False otherwise.
        """
        return (self._bolt1 == 0 and self._bolt2 == 0)

    def clue(self): 
        """
        Provides a hint about the current lock state without revealing exact values.

        :return: str
            A clue describing whether both bolts are locked or if one might be unlocked.
        """
        if(self._bolt1 == 1 and self._bolt2 == 1):
            return "...it seems like it's completely locked"
        else: 
            return "You jiggle the door...it seems like one of the bolts is unlocked"
        

    def success(self):
        """
        Determines the outcome of the user's interaction with the door.

        :return: str
            A success message if the door is unlocked,
            otherwise a clue indicating the current state.
        """
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        return self.clue()