# Count the number of prime numbers less than a non-negative number, n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0

import math
class Solution:
    def countPrimes(self, n):
        if n<=2:
            return 0
        # the number x is represented by a[x]
        a = [1] * n
        # ignore 0 and 1
        a[0] = a[1] = 0
        nsqrt = math.ceil(math.sqrt(n))
        for i in range(2, nsqrt + 1):
            if not a[i]:
                continue
            j = int(math.pow(i, 2))
            while j < n:
                a[j] = 0
                j += i
        return sum(a)

