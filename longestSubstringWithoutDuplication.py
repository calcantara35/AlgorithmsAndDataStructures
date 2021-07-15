"""
Write a function that takes in a string and returns its longest substring without duplicate characters
You can assume that there will only be on longest substring without duplication
Sample Input = "abcabcbb"
Sample output = 3

Brute force:
Using "abcabcbb" as input string
suppose we are given the input string. We start from the first character 'a' and enumerate and check all the substrings starting from it.
Then we move forward to the second character and enumerate all the substrings starting from character b
And so on...

But more optiomal solution:
Use a set for duplicates issue -> will be a set of subsrings
use sliding window technique to reduce time complexity and iterate through array once 
maintain longest substring in a var
"""
# Time and space -> O(n)

# our right pointer will be changing every time we iterate through the array, big note!! -> so declare the right pointer within the iteration

def lengthOfLongestSubString(s: str):
    characterSet = set()
    leftPointer = 0
    result = 0
    
    for rightPointer in range(len(s)):
        # right pointer will go through every single character
        # if we get to a duplicate character , we need to update our window and set
        # while the character we are iterating on so string[r] is already in the character set
        while s[rightPointer] in characterSet:
            characterSet.remove(s[leftPointer])
            leftPointer += 1
        characterSet.add(s[rightPointer])
        """
        Reason for right - left + 1
        let's supose your string is "abca"
        you can see that the longest string is "abc", wich starts at string[0] and ends at string [2].
        if you do simply right (wich is 2) minus left ( 0 ) you would get that the size of the string is 2, while in reality it is 3.
        that's why you need the plus 1 
        """
        # taking the which ever value is bigger | a way to keep track if the largest substring
        result = max(result, rightPointer - leftPointer + 1)

    return result

lengthOfLongestSubString('pwwkew')

