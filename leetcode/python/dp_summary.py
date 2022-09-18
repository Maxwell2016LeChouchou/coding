# # 1. Fibonacci Sequence
# # 1.1 Recursive
# def fib_recursive(n):
#     f = [0 for i in range(n)]
#     f[0], f[1] = 1, 1
#     for i in range(2, n):
#         f[i] = f[i-1]+f[i-2]
#     return f[-1]

# print(fib_recursive(6))
  
#1.2 DP

# def fib_dp(n):
#     a, b = 1, 1
#     count = 2
#     while count < n:
#         c = a + b
#         a = b
#         b = c
#         count += 1
#     return c

# print(fib_dp(6))

# 2. Maximum Value Continuous Subsequence
# {-1, -1, -2, 3, 5, -1, 4, -2}
# solution: A[j] = max{A|j-1|+arr[j], arr[j]}

# import numpy as np

# def get_max_subseq(arr):
    
#     if arr is None or len(arr) == 0:
#         return 0
    
#     n = len(arr)
#     pos_num = 0
#     for i in range(n):
#         if arr[i] >= 0:
#             pos_num += 1
#     if pos_num == n:
#         return sum(arr)

#     dp = [0 for i in range(n)]
#     dp[0] = arr[0]

#     for i in range(1, n):
#         dp[i] = max(dp[i-1]+arr[i], arr[i])

#     return max(dp)

# arr = [-1, 2, 3, -1, 4, 3, 2, -7, -3]
# print(get_max_subseq(np.array(arr)))


# Coin Change Problem
# Problem: There are n categories coins, values are 1 = V1 < V2 < V3 < ... < Vn, how to change coin for least number of coins
# Analysis: When price value is j, the least number of coins is M(j)
# DP list: [M(1), M(2).... M(j),.... M(C)]
# Algorithm: M(j) = min{M(j-V1)+1, M(j-V2)+1, M(j-V3)+1, ..., M(j-Vn)+1}

import sys
def min_coin_change(arr, C):

    if len(arr)==0 or None:
        return 0
    # dp[i]: minimum number of coin for amount i (i=0,1,2,3,...,C)
    dp = [sys.maxsize for i in range(C+1)]
    dp[0] = 0
    for i in range(1,C+1):
        j = 0
        while j < len(arr) and i >= arr[j]:
            if dp[i] >= dp[i-arr[j]]+1:
                dp[i] = dp[i-arr[j]]+1  
            j+=1            
    return dp[-1]

arr = [2,3,4,6,8]
C = 16
print(min_coin_change(arr, C))


# def min_coin_change2(arr, C):
#     if len(arr) == 0 or None:
#         return 0
#     dp = [sys.maxsize for i in range(C+1)]
    