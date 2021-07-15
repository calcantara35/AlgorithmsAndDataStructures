"""
Given a string s, find the longest palidromic substring in s. You may assume that the maximum lenght of s is 1000
example 1:
Input: "babad"
Output: "bab"
Note: "aba" is alos a valid answer
"""

def longestPalidrome(string):
    result = ""
    resultLength = 0

    for i in range(len(string)):
        # check odd length palidromes
        left, right = i, i
        while left >= 0 and right <= len(string) and string[left] == string[right]:
            # we know its a plindrome
            if right - left + 1 > resultLength:
                result = string[left: right+1]
                resultLength = right - left + 1
            left -= 1
            right += 1
        # event length palidromes
        left, right = i, i + 1
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if right - left + 1 > resultLength:
                result = string[left: right + 1]
                resultLength = right - left + 1
            left -= 1
            right += 1
    return result



string = longestPalidrome("racecar")