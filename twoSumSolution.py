"""
    Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to "target"
    You may assume that each input would have exactly one solution, and you may not use the same element twice!
    You can return the answer in any order

    Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0,1]
"""


def twoSum(nums, target):
    # empty hashmap at first,
    # The Key of hashmap will be the value at the current iteration from the array
    # the value of the hashmap at specific key will be the index of the current iteration
    hashMap = {}
    # enumerate lets you have keyvalue pairs (tuple) and for this case, the i will be the index and n will be the value at that index
    for i,n in enumerate(nums):
        # simple equation to find the potential match
        potential = target - n
        if potential in hashMap:
            # returns the index of the potential match with the index at the current iteration the potential match was found
            return [hashMap[potential], i]
        # if not in the hashmap, we add to the hashmap.
        # key will be the value at the specific iteration and the value will be the index at the specific iteration
        hashMap[n] = i



def twoNumberSum(array, targetSum):
    """
        This solution gives you the actualy value that sums up to the target number in the array
        It wont give you the index of those values. It will return an array with the actual values.
    """
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


array = [2, 7, 11, 15]
targetNum = 9
twoNumberSum(array, targetNum)
twoSum(array, targetNum)
