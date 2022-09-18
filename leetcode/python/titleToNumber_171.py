# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701

def titleToNumber(s):
	acc = 0
	n = len(s) - 1
	for i in range(len(s)):
		acc += 26 ** n * (ord(s[i]) - 64)
		n -= 1
	return acc

s = "AC"
print(titleToNumber(s))