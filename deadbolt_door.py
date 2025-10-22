from door import Door
import random
class DeadboltDoor(Door):
    def __init__(self):
        """Attributes: 
        _bolt1: int
        _bolt2: int
        1 is locked
        0 is unlocked"""

        # random bolt 1 from 0 to 1
        self._bolt1 = random.randint(0, 1)
        # if bolt1 is already unlock, then the second one should not be unlocked
        if(self._bolt1 == 0):
            self._bolt2 = 1
        # otherwise, randomly choose bolt2
        else:
            self._bolt2 = random.randint(0, 1)
    
    def examine_door(self): 
        return "You have encountered a door with two deadbolts. Both need to be unlocked to open the door, but you can't tell if each one is locked or unlocked."
    
    def menu_option(self):
        return  """
1. Toggle bolt 1
2. Toggle bolt 2"""
    
    def get_menu_max(self): 
        return 2
    
    def attempt(self, option):
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
        return (self._bolt1 == 0 and self._bolt2 == 0)

    def clue(self): 
        if(self._bolt1 == 1 and self._bolt2 == 1):
            return "...it seems like it's completely locked"
        else: 
            return "You jiggle the door...it seems like one of the bolts is unlocked"
        

    def success(self):
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        return self.clue()