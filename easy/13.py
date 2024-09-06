# LEETCODE 13
# Title: Roman to integer
# Difficulty: Easy
# Solved on: 03/09/2024

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 
--------------------------------------------------------------
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
--------------------------------------------------------------

--------------------------------------------------------------
Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
--------------------------------------------------------------

--------------------------------------------------------------
Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
--------------------------------------------------------------
 
--------------------------------------------------------------
Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
--------------------------------------------------------------

"""

# This function creates a list of the corresponding digits
def convert(s: str) -> list:
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return [dic[c] for c in s]

# This function gives the number from the oredered list of digits,
# according to the positional rules of romans numbers
def roman(numbers: list) -> int:
    if numbers:
        l = len(numbers)
        if l==1:
            return numbers[0]
        else:
            tot = 0
            i = 0
            while i<l-1:
                p = numbers[i]
                d = numbers[i+1]
                if p<d:
                    tot += (d-p)
                    i+=2
                else:
                    tot += p
                    i+=1
            if i==l-1:
                tot += numbers[i]
            return tot
    else:
        return None

# Since we know that the "strange" numbers are only six,
# we can put them first in the dictionary and then compute directly
# without the rules of position
def strong_convert(s: str) -> int:
    dic = {
        "CM":900,
        "CD":400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    tot = 0
    for roman, values in dic.items():
        print(s, tot)
        i = s.count(roman)
        tot += values * i
        s = s.replace(roman, "")
    return tot

def roman_to_arabic(s: str) -> int:
    #return strong_convert(s) 
    return roman(convert(s))


if __name__ == "__main__":
    print(roman_to_arabic("MCMXCIV")) #Expected: 1994




