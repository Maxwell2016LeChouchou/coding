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