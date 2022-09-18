# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Solution 1:
# def isAnagram(s, t):
#     return sorted(s) ==  sorted(t)


# Solution 2:
def isAnagram(s, t):
    dictionary = {}

    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
            # print(i)
            # print(dictionary[i])
    
    for i in t:
        if i in dictionary:
            dictionary[i] -= 1
            print(dictionary[i])
        else:
            return False
    
    for val in dictionary.values():
        if val != 0:
            return False
    
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
        
    