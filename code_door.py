from door import Door
import random

class CodeDoor(Door): 
    def __init__(self):
        """
        Initializes the CodeDoor object with the following attributes:
        - _correct_code: char[] - The randomly generated correct code to unlock the door.
        - _input: char[] - The user's current input code, initialized to a random state.
        """
        code = { 0: 'O', 1: 'X'}
        self._correct_code = []
        self._input = []
        for index in range(3): # Generate a 3-character code
            # random initialize character 'X' or 'O' from code array
            self._correct_code.append(code[random.randint(0,1)])
            self._input.append(code[1 - random.randint(0,1)])
    def examine_door(self): 
        """
        Provides a description of the door.
        :return: A string describing the door as one with a coded keypad.
        """
        return "A door with a coded keypadwith three characters. Each key toggles av alue with an ‘X’ or an ‘O'"
       
    
    def menu_option(self):         
        """
        Displays the menu options for interacting with the door.
        :return: A string listing the available actions (pressing keys 1, 2, or 3).
        """
        return """1. Press Key 1
2. Press Key 2
3. Press Key 3"""
    
    def get_menu_max(self): 
        """
        Returns the maximum number of menu options available for the door.
        :return: An integer representing the maximum menu option (3 in this case).
        """
        return 3
    
    def attempt(self, option):
        """
        Toggles the character at the specified position in the user's input code.
        :param option: int - The key pressed by the user (1, 2, or 3).
        :return: A string describing the action taken by the user.
        """
        option -= 1
        if(self._input[option] == 'O'):
            self._input[option] = 'X'
        else: 
            self._input[option] = 'O'
         # Provide feedback based on the key pressed.
        match option:
            case 0: 
                return "You pressed key 1"
            case 1: 
                return "You pressed key 2"
            case 2: 
                return "You pressed key 3"
    
    def is_unlocked(self):
        """
        Checks if the door is unlocked by comparing the user's input to the correct code.
        :return: True if the input matches the correct code, False otherwise.
        """        
        if(self._correct_code == self._input):
            return True
        return False

    def clue(self): 
        """
        Provides a clue to the user if the door remains locked.
        :return: A string with either:
                 - The keys that are correct, or
                 - The number of correct characters in the input.
        """
        # Randomly choose one of two clue types.
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
        """
        Determines the outcome of the user's interaction with the door.
        :return: A success message if the door is unlocked, or a clue if it remains locked.
        """
        if(self.is_unlocked()):
            return "Congratulation, you opened the door"
        else: 
            return self.clue()