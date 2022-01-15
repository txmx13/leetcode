"""
  Challenge: 14. Longest Common Prefix 
  Desc: 
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) < 1 or len(strs) > 200:
            print("List must have between 1 to 200 elements")
        else:
            strs.sort()
            solution = ''
            i = 0
            
            for char in strs[0]:
                if char == strs[-1][i]:
                    solution += char
                    i += 1
                else:
                    break
            
            return solution
