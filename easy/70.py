# LEETCODE 70
# Title: Climbing Stairs
# Difficulty: Easy
# Solved on: 07/09/2024
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 

--------------------------------------------------------------
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
--------------------------------------------------------------

--------------------------------------------------------------
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
--------------------------------------------------------------
 
--------------------------------------------------------------
Constraints:
1 <= n <= 45
--------------------------------------------------------------

"""
# this is the same problem of
# the n-th item of Fibonacci's sequence

# recursive solution
def climb_rec(n):
    if n==0 or n==1:
        return 1
    return climb_rec(n-1)+climb_rec(n-2)


# dinamic programming solution
def climb_dp(n):
    dp = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-2]+dp[i-1]
    return dp[n]

# clever solution
def climb(n):
    if n==0 or n==1:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n+1):
        temp = curr
        curr = curr + prev
        prev = temp
    return curr

