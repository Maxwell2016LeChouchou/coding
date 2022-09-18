# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. T
# hose numbers for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.
# Example: 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def isHappy(self,n):
        return self.recursion(n, [])
    def recursion(self, n, existingSum):
        sum_ = 0
        for digit in list(str(n)):
            sum_ = sum_ + int(digit)**2
        if sum_ == 1:
            return True
        if sum_ not in existingSum:
            existingSum.append(sum_)
        else:
            return False
        return self.recursion(sum_,existingSum)



            