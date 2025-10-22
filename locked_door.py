from door import Door
import random
class LockedDoor(Door):
    def __init__(self):
        """Attributes: 
        _key_location: int
        _input: int"""

        self._key_location = random.randint(1,self.get_menu_max())
        self._input = 0
    def examine_door(self): 
        return "You have encountered a locked door. The key is hidden nearby. Look around for the key."
    
    def menu_option(self):
        return """
1. Look under the mat
2. Look under the flower pot
3. Look under the fake rock"""
    
    def get_menu_max(self): 
        return 3
    
    def attempt(self, option):
        self._input = option
        match option: 
            case 1: 
                return "You looked under the mat"
            case 2: 
                return "You looked under the flower pot"
            case 3: 
                return "You looked under the fake rock"
    
    def is_unlocked(self):
        if(self._input == self._key_location):
            return True
        return False

    def clue(self): 
        return "Look somewhere else"

    def success(self):
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()