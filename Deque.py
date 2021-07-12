class Deque:

    def __init__(self):
        self.items = []

    # add to either side and remove from either side
    # we need to specifiy the locaiton
    # we are using the left side of the list to represent front of deque

    def addToFront(self, item):
        """
        Inserting to 0th index of list
        Run time is linear O(n) because every time you insert into front of list, the items are shifted to the right
        """
        self.items.insert(0, item)

    def addToBack(self, item):
        """
        Takes in an item as a parameter and appends the item to the end of the list that is representing the deque
        Runtime -> Constant time O(1)
        """
        self.items.append(item)

    def removeFromFront(self):
        """
        Removes and returns the item in the 0th index of the list, which represents the front of the deque

        Run time -> O(n) Linear time because once you remove the first item from the list at 0th index
        , the items need to shift to the left 
        """
        if self.items:
            return self.items.pop(0)
        return None

    def removeFromBack(self):
        """
        Removes and returns the last item in the list which represents the rear of the list.
        """
        if self.items:
            return self.items.pop()
        return None

    def peekFront(self):
        """
        Returns the value found at the -th index of the list, which is the front of the Deque
        Constant run time since we are just indexing in the list
        """
        if self.items:
            return self.items[0]
        return None

    def peekRear(self):
        """
        Returns the value found at the last index of the list
        The run time is constant because of just indexing
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the count of the list
        Constant time
        """
        return len(self.items)

    def isEmpty(self):
        """
        Compares the list of items to an empty list.
        Returns true if it is empty, returns false if its full
        Constant time.
        """
        return self.items == []


"""
Prompt - Palindrome checker
Using a deque data structure, write a function that takes in an input string and returns:
True if the string is a palindrome
False if it is not
Palidrome is a word thats spelled the same backwards and forwards
Examples:
Mom
Level
Kayak
"""

def is_palidrome(string):
    
    deque = Deque()

    for char in string:
        # at to the rear since it adds the items in constant time
        deque.addToBack(char)
    
    # if the size is 1 or 0, that means the string is a palidrome
    while deque.size() >= 2:
        front_most_item = deque.removeFromFront()
        rear_most_item = deque.removeFromBack()

        if front_most_item != rear_most_item:
            return False
            
    return True


is_palidrome("mom")
       

        
    