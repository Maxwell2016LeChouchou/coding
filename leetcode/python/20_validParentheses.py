# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def isValid(s):
    stack = []
    match = {"(":")", "[":"]", "{":"}"}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack)>0 and char == match[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack)==0

s = "{{[(]}}"
print(isValid(s))
