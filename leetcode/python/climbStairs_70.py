# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Dynamic Programming

# One can reach ith step in one of the two ways:
# 1. Take a single step from (i-1)th step
# 2. Taking a step of 2 from (i-2)th step

# so, the total number of ways to reach ith is equal to sum of ways of reaching (i-1)th step
# and ways of reaching (i-2)th step

# Let dp[i] denotes the number of ways to reach on ith step:
# dp[i] = dp[i-1] + dp[i-2]


def climbStairs(n):
    if n < 1:
        return 1
    dp = [None]*(n+1)
    print(dp)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

n = 3
dp = climbStairs(n)
print(dp)
