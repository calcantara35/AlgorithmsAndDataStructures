"""
Youre given an array of integers where each integer represents a jump of its valuye in the array. For instance, the integer 2 represents a jump of
two indices forward in the arry, and the integer -3 represents a jump of three indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array.
Similarly, a jump of 1 at the last index in the array brings us to index 0

Write a function that returns a boolean representing whether the jumps in the array form a single cycle.
A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back
on the starting index

Sample input = [2, 3, 1, -4, -4, 2]
sample output = true
"""

def hasSingleCycle(array):
    # kind of like a counter of how many elements we have visited in the array based on the jumps
    numElementsVisited = 0
    # current index is used to track the position we are in based on a jump
    currentIndex = 0
    while numElementsVisited < len(array):
        # if we visited more than 1 element and the current index is 0, we know we are dealing with multiple cycles
        if numElementsVisited > 0 and currentIndex == 0:
            return False
        numElementsVisited += 1
        # jump through elements
        currentIndex = getNextIndex(currentIndex, array)
    # if its true, we are back at the start and we only have one cycle
    return currentIndex == 0

def getNextIndex(index, array):
    """
    When we are getting the next index, we need to see how many indices we are jumping forward or backward
    """
    jump = array[index]
    # we can have any int in this array | we want to wrap around the array so we are using the modular operator
    nextIndex = (index + jump) % len(array)
    # we need to handle the case where its a negative number -> so we add the negative number and the len of the array to get the positive version
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)