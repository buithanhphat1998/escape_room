from door import Door
import random

class CodeDoor(Door): 
    def __init__(self):
        """Attributes: 
        _correct_code = char[]
        _input = char[]"""
        code = { 0: 'O', 1: 'X'}
        self._correct_code = []
        self._input = []
        for index in range(3):
            # random initialize character 'X' or 'O' from code array
            self._correct_code.append(code[random.randint(0,1)])
            self._input.append(code[1 - random.randint(0,1)])
    def examine_door(self): 
        return "A door with a coded keypadwith three characters. Each key toggles av alue with an ‘X’ or an ‘O'"
       
    
    def menu_option(self):
        return """1. Press Key 1
2. Press Key 2
3. Press Key 3"""
    
    def get_menu_max(self): 
        return 3
    
    def attempt(self, option):
        option -= 1
        if(self._input[option] == 'O'):
            self._input[option] = 'X'
        else: 
            self._input[option] = 'O'

        match option:
            case 0: 
                return "You pressed key 1"
            case 1: 
                return "You pressed key 2"
            case 2: 
                return "You pressed key 3"
    
    def is_unlocked(self):
        if(self._correct_code == self._input):
            return True
        return False

    def clue(self): 
        match random.randint(0,1):
            case 0: 
                res = ""
                for index in range(3):
                    if(self._input[index] == self._correct_code[index]):
                        res += f"Key {index+1} is correct\n"
                return res
            case 1: 
                count = 0
                for index in range(3):
                    if(self._input[index] == self._correct_code[index]):
                        count+=1
                return f"The number of correct characters: {count}"

    def success(self):
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()