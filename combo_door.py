from door import Door
import random

class ComboDoor(Door):
    def __init__(self):
        """Attributes: 
        _correct_value: int - radomized value from 1-10
        _input_value: int - input value from 1-110 from user
        """
        self._correct_value = random.randint(1,10)
        self._input_value = 0
    def examine_door(self): 
        return "A door with a combination lock. You can spin the dial to a number 1-10"
    
    def menu_option(self):
        return "Enter # 1-10:"
    
    def get_menu_max(self) -> int: 
        return 10
    
    def attempt(self, option):
        self._input_value = option
        return f"You turn the dial to...{option}"
        
    
    def is_unlocked(self):
        if(self._input_value == self._correct_value):
            return True
        return False

    def clue(self): 
        if(self._input_value > self._correct_value):
            return "Too high!"
        elif(self._input_value < self._correct_value):
            return "Too low!" 

    def success(self):
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()