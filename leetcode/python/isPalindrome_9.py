# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Solution 1
def isPalindrome_1(x):
    if x < 0:
        return False
    a = x
    b = 0

    while x:
        b = b*10
        b = b+x%10
        x//=10
    return a==b


#Solution 2 
def isPalindrome_2(x):
    if x < 0:
        return False 
    else:
        y = int(str(x)[::-1])
        return x==y
    
x = 1234321
print(isPalindrome_1(x))

