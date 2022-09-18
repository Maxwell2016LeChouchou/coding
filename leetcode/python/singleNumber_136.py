# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# 136 Single Number

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

from collections import Counter

def singleNumber(nums):
    i = Counter(nums)
    for key, value in i.items():
        if value == 1:
            return key

nums = [1,2,3,3,2,2,1,4,5,5]
print(singleNumber(nums))
