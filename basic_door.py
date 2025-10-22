from door import Door
import random
class BasicDoor(Door):
    def __init__(self):
        """Attributes: 
        _state: int
        _input: int """
        self._state = random.randint(1,self.get_menu_max())
        self._input = 0
    def examine_door(self):
        return "You have encountered a door that is either pushed to open, or pulled"

    def menu_option(self):
        return """
1. Push
2. Pull"""

    def get_menu_max(self):
        return 2
    
    def attempt(self, option):
        self._input = option
        match option: 
            case 1: 
                return "You push the door"
            case 2: 
                return "You pull the door"

    def is_unlocked(self):
        if(self._input == self._state):
            return True
        return False
    def clue(self):
        return "Try the other way"
    
    def success(self):
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()

