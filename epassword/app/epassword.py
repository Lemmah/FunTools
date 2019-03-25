#!/usr/bin/env python3

from pyperclip import copy as pcopy
from random import choice, randint
from string import ascii_letters, digits, punctuation

class Password():
    """
    Password Blueprint: defines how a password should look like.
    """    
    def __init__(self, length = 16, properties = ["a", "d", "p"]):
        self.length = length
        self.properties = properties
        self.value = self.__value
  
    @property
    def __char_range(self):
        char_range = ""
        char_range += ascii_letters if "a" in self.properties else ""
        char_range += digits if "d" in self.properties else ""
        char_range += punctuation if "p" in self.properties else ""
        return char_range
    
    @property
    def __value(self):
        value = "".join(choice(self.__char_range) for c in range(self.length))
        value = value.lower() if "l" in self.properties else value
        value = value.upper() if "u" in self.properties else value
        return value

    def copy(self):
        pcopy(str(self))
        return "copied to clipboard!"

    def __repr__(self):
        return self.value
