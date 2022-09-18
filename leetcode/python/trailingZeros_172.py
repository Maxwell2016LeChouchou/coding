
# Given an integer n, return the number of trailing zeroes in n!.

# Follow up: Could you write a solution that works in logarithmic time complexity?


# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0


# # Solution 1: My Solution
# import math

# def trailingZeros(n):
#     if n ==  0:
#         return 0
#     else:
#         nums = n * math.factorial(n-1)
#         s = str(nums)
#         array = []
#         print(s)
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == "0":
#                 array.append(s[i])
#             else:
#                 break
#     return len(array)

# n = 10
# print(trailingZeros(n))


# Another Solution:
# trailing zeros will occur when 5 multiply by 2, so after every 5 get 1 zero
def trailingZeros(n):
    if n == 0:
        return 0
    count = 0
    while n:
        n //= 5
        count += n
    return count

n = 10
print(trailingZeros(n))
