from abc import ABC, abstractmethod
import string
class Door(ABC):
    @abstractmethod
    def examine_door(self) -> int: 
        """
        Provides a description of the door.
        :return: An integer representing the door's description (implementation-specific).
        """
        pass
    
    @abstractmethod
    def menu_option(self) -> string:
        """
        Displays the menu options for interacting with the door.
        :return: A string listing the available actions for the door.
        """
        pass
    
    @abstractmethod
    def get_menu_max(self) -> int: 
        """
        Returns the maximum number of menu options available for the door.
        :return: An integer representing the maximum menu option.
        """
        pass
    
    @abstractmethod
    def attempt(self, option) -> string:
        """
        Records the user's attempt to interact with the door and provides feedback.
        :param option: The user's chosen action (implementation-specific).
        :return: A string describing the action taken by the user.
        """
        pass
    
    @abstractmethod
    def is_unlocked(self) -> bool:
        """
        Checks if the door is unlocked.
        :return: True if the door is unlocked, False otherwise.
        """
        pass

    @abstractmethod
    def clue(self) -> string: 
        """
        Provides a clue to the user if the door remains locked.
        :return: A string suggesting the next step or hint.
        """
        pass

    @abstractmethod
    def success(self) -> string:
        """
        Determines the outcome of the user's interaction with the door.
        :return: A success message if the door is unlocked, or a clue if it remains locked.
        """
        pass