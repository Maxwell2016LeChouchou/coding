# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        bij,j,s = {}, 0, s.split(' ') # Bijection, pointer and splitting input string by space char
        keys,vals = [],[] # Keys and values arrays so that list(bij.keys()/bij.values()) doesn't need to be called every iteration
        if len(s) != len(pattern): # Check if pattern and string are of same length. Or else return False
            return False
        for string in s:
            if pattern[j] not in keys: # Check if we have already come across char in the pattern
                if string in vals:  # Checking if the string that the char is mapped to doesn't exist in the values either
					# If it does exist, that would mean there are two chars in the pattern which map to 
					# the same string which cannot happen. Hence, return False
                    return False
				# Append string and char to respective vals and keys arrays
                keys.append(pattern[j])
                vals.append(string)
                bij[pattern[j]] = string #Create new key in the bijections dictionary
            if string != bij[pattern[j]]: # Check if the string in current iteration is the same that the char in pattern is mapped to. If it's not, that means there are two different strings which are mapped to the same character in the pattern, which is again impossible. Hence, return false
                return False
            j += 1
        return True