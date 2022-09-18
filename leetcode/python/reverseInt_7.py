# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

def reverse(x):
    x = int(str(x)[::-1] if x>0 else -int(str(-x)[::-1]))
    return x if x < 2147483648 and x >= -2147483648 else 0

x = -753
print(reverse(x))