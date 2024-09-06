# LEETCODE 14
# Title: Longest Common Prefix
# Difficulty: Easy
# Solved on: 05/09/2024

"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

 
--------------------------------------------------------------
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
--------------------------------------------------------------

--------------------------------------------------------------
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
--------------------------------------------------------------
 
--------------------------------------------------------------
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
--------------------------------------------------------------

"""


def longest_common_prefix(strs: list) -> str:
        if len(strs) == 0:
             return ""
        p = ""
        for cs in zip(*strs):
            # cs is a tuple with all the chars at the i-th position
            if len(set(cs)) != 1: # if they are not the same
                break             # the common prefix is finished
            p += cs[0]            # otherwise it continues by adding the chars
        return p
