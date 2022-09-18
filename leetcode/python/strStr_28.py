# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

def strStr(haystack, needle):
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    else:
        w = haystack.index(needle)

        return w

haystack = "maxwell"
needle = "we"

print(strStr(haystack,needle))