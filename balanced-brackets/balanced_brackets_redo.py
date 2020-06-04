import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):

    bracket_dict = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    opening_brackets = set()
    opening_brackets.update(['{', '[', '('])
    
    string_array = list(s)
    
    stack = [string_array[0]]

    for character in string_array[1:]:
        if character in opening_brackets:
            stack.append(character)
        elif character in bracket_dict:
            opening_bracket = stack.pop()
            if opening_bracket != bracket_dict[character]:
                return 'NO'
    
    if len(stack) > 0:
        return "NO"
    else:
        return 'YES'