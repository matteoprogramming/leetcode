# LEETCODE 9
# Title: Palindrome number
# Difficulty: Easy
# Solved on: 03/09/2024

"""
Given an integer x, return true if x is a palindrome,
and false otherwise.
Given an integer x, return true if x is a 
 
--------------------------------------------------------------
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
--------------------------------------------------------------

--------------------------------------------------------------
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. 
From right to left, it becomes 121-.
Therefore it is not a palindrome.
--------------------------------------------------------------

--------------------------------------------------------------
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
--------------------------------------------------------------

--------------------------------------------------------------
Constraints:
-231 <= x <= 231 - 1
--------------------------------------------------------------

"""


def is_palindrome(n: int) -> bool:
    s = str(n)
    l = len(str(n))
    for i in range(l//2):
        # if the number is even, not problem
        # if the number is odd, not problem
        # because we will not consider the central number
        #print(s[i], s[l-i-1])
        if s[i]!=s[l-i-1]:
            return False
    return True

if __name__ == "__main__":
    print(is_palindrome(1234321)) #Expected: True
