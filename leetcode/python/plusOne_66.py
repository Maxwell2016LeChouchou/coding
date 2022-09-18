# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:

# Input: digits = [0]
# Output: [1]



def plusOne(digits):

    n = ""
    for i in digits:
        n = n+str(i)

    n = int(n)
    n = n+1
    n = str(n)
    res = []
    for i in n:
        res.append(int(i))
    return res

digits = [1,2,3]
print(plusOne(digits))
