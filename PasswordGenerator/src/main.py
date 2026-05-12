import random
import string
from typing import List
from abc import ABC, abstractmethod

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass


    class RandomPasswordGenerator(PasswordGenerator):
        def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
            self.length = length
            self.characters = string.ascii_letters
            if include_numbers:
                self.characters += string.digits
            if include_symbols:
                self.characters += string.punctuation

        def generate(self) -> str:
            return ''.join(random.choice(self.characters) for _ in range(self.length))
