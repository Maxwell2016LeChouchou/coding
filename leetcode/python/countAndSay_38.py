# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
 

# Example 1:

# Input: 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:

# Input: 4
# Output: "1211"

def countAndSay(n):
    if n is 1:
        return "1"
    
    previous = countAndSay(n-1)

    res = ""
    i = 0
    while i < len(previous):
        num = previous[i]
        num_count = 1
        i += 1
        while i < len(previous) and num == previous[i]:
            num_count += 1
            i += 1
        res += "%s%s" % (num_count, num)
    return res

n = 4
print(countAndSay(4))


