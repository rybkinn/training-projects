"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        if not (1 <= len(s) <= 15):
            return False
        allowed_symbols = "IVXLCDM"
        if not all(char in allowed_symbols for char in s):
            return False
        symbol_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        char_values = []
        for i, char in enumerate(s):
            if i == 0:
                char_values.append(symbol_value[char])
                continue
            last_val = char_values.pop()
            if last_val < symbol_value[char]:
                value = symbol_value[char] - last_val
                char_values.append(value)
            else:
                char_values.append(last_val)
                char_values.append(symbol_value[char])
        return sum(char_values)


sol = Solution()
assert sol.romanToInt("III") == 3
assert sol.romanToInt("IV") == 4
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
