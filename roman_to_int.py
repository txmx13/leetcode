"""
  Challenge: Roman Numeral to Integer 
  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

  Symbol       Value
  I             1
  V             5
  X             10
  L             50
  C             100
  D             500
  M             1000
  For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

  Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

  I can be placed before V (5) and X (10) to make 4 and 9. 
  X can be placed before L (50) and C (100) to make 40 and 90. 
  C can be placed before D (500) and M (1000) to make 400 and 900.
  Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = []
        i = 0
        
        for symbol in s:
            if i == len(s) - 1:
                values.append(self.symbol_num_map(symbol))
            elif (symbol == 'I' and s[i+1] == 'V') or (symbol == 'I' and s[i+1] == 'X'):
                neg_i = -self.symbol_num_map(symbol)
                values.append(neg_i)
            elif (symbol == 'X' and s[i+1] == 'L') or (symbol == 'X' and s[i+1] == 'C'):
                neg_x = -self.symbol_num_map(symbol)
                values.append(neg_x)
            elif (symbol == 'C' and s[i+1] == 'D') or (symbol == 'C' and s[i+1] == 'M'):
                neg_c = -self.symbol_num_map(symbol)
                values.append(neg_c)
            else:
                values.append(self.symbol_num_map(symbol))

            i += 1
        
        sum = 0
        
        for num in values:
            print(num)
            sum += num
        
        return sum

    def symbol_num_map(self, symbol):
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        return map.get(symbol)

