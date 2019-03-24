#!/usr/bin/env python3

from random import choice, randint
from string import ascii_letters, digits, punctuation

class Password():
    """
    Password Blueprint: defines how a password should look like.
    """    
    def __init__(self, length = 16, properties = ["a", "d", "p"]):
        self.length = length
        self.properties = properties

    @property
    def value(self):
        password = "".join(choice(self._char_range) for c in range(self.length))
        password = password.lower() if "l" in self.properties else password
        password = password.upper() if "u" in self.properties else password
        return password
  
    @property
    def _char_range(self):
        password_range = ""
        password_range += ascii_letters if "a" in self.properties else ""
        password_range += digits if "d" in self.properties else ""
        password_range += punctuation if "p" in self.properties else ""
        return password_range
    
    def __repr__(self):
        return self.value
