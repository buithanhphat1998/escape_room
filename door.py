from abc import ABC, abstractmethod
import string


"""
Methods: 
examine_door(self) – returns a string description of the door.
menu_options(self) – returns a string of the menu options that user can choose from when
attempting to unlock the door.
get_menu_max(self) – returns the number of options in the above menu.
attempt(self, option) – passes in the user’s selection from the menu. Uses that value to
update the attributes that are needed to determine whether the user has unlocked the door
(which is done in the is_unlocked method below). Returns a string describing what the
user attempted.
is_unlocked(self) – checks to see if the door was unlocked, returns true if it is, false
otherwise.
clue(self) – returns the hint that is returned if the user was unsuccessful at their attempt.
success(self) – returns the congratulatory message if the user was successful
"""

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