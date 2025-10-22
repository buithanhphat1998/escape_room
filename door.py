from abc import ABC, abstractmethod
import string
class Door(ABC):
    @abstractmethod
    def examine_door(self) -> int: 
        pass
    
    @abstractmethod
    def menu_option(self) -> string:
        pass
    
    @abstractmethod
    def get_menu_max(self) -> int: 
        pass
    
    @abstractmethod
    def attempt(self, option) -> string:
        pass
    
    @abstractmethod
    def is_unlocked(self) -> bool:
        pass

    @abstractmethod
    def clue(self) -> string: 
        pass

    @abstractmethod
    def success(self) -> string:
        pass