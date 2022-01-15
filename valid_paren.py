"""
  *** In progress *** 
  
  Challenge: 20. Valid Parentheses
  Desc: 
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        i = 0
        while i < len(s):            
            if i == len(s) - 1:
                return True
            
            elif self.get_expected_char(s[i]) != s[i+1]:
                return False
             
            else:
                i += 2
                              
    def get_expected_char(self, c):
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        return map.get(c)
