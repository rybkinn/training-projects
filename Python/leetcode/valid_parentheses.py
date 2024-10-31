"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        valid_brackets = "()[]{}"
        stack = []
        for c in s:
            # open
            if c in valid_brackets[::2]:
                stack.append(c)
                continue
            # close
            if c in valid_brackets[1::2] and stack:
                bracket_index = valid_brackets.index(c)
                if valid_brackets[bracket_index - 1] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        return False


sol = Solution()
assert sol.isValid("()") == True
assert sol.isValid("()[]{}") == True
assert sol.isValid("(]") == False
assert sol.isValid("([])") == True
assert sol.isValid("(())") == True
assert sol.isValid("([)]") == False
assert sol.isValid(")(") == False
assert sol.isValid("({{{{}}}))") == False
