# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# LEETCODE link: https://leetcode.com/problems/valid-parentheses/description/

# def valid_parenthesis(s):
#     stack = []
#     map = { ')':'(' , '}':'{' , ']':'[' }
#     for bracket in s:
#         if not map.get(bracket):
#             stack.append(bracket)
#         elif stack and stack[-1] == map[bracket]:
#             stack.pop()
#         else:
#             return False
#     if stack:
#         return False
#     return True


def valid_parenthesis(s): # Simpler Version
    stack = []
    map = { ')':'(' , '}':'{' , ']':'[' }
    brackets = [')','(','}','{',']','[']

    for current in s:
        if current in brackets: # ignores all other characters
            if current in map:
                if stack and stack[-1] == map[current]: # if 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(current)
        else: continue

    return (False if stack else True)


# Example Usage:
s = "(hgfhfghfghfgh{gfdhfghgh})(gfhgfh)ghfghgfh{fgh}ghgfhfg[djhfs{sdkfjsdkf}](kdfjdskfj) [{({[[(({({([([()])])})}))]]})}]"

from time import time

start = time()
print(valid_parenthesis(s))
end = time()
print(f"{((end- start)*1000):.3f} milli-sec\n")