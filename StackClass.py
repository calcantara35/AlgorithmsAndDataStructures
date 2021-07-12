class Stack:

    # Need a python list to represent stack

    def __init__(self):
        self.items = []

    # add items to stack
    def push(self, item):
        """
        Accepts item as a param and appends it to the end of the list
        Returns void

        Runtime -> O(1) Constant time -> appending to the end of the list happens in constant time
        """
        self.items.append(item)

    # remove item and display the removed item
    def pop(self):
        """
        Removes and returns the last item from the list, which is also the top item of the stack.

        Runtime -> O(1) Constant time -> indexing to the last item in the list and returning it
        """
        if self.items:
            return self.items.pop()

        return None

    # peek at what the next item that is going to be removed
    def peek(self):
        """
        This method returns the last item in the list, which is the item at the top of stack
        Runtime -> Constant O(1) -> indexing into a list is contstant time
        """
        if self.items:
            return self.items[-1]
        return None

    # how many items in stack?
    def size(self):
        """
        Returns the size of the list that is representing the Stack
        Run Time -> Constant time -> O(1) because finding the length of a list is also in constant time
        """
        return len(self.items)

    # is the stack empty??
    def isEmpty(self):
        """
        Returns a boolean value describing whether or not the stack is empty
        RunTime -> Constant time O(1) -> testing for equality happens in constant time
        """
        return self.items == []


# Challenge ->
# Create a function that takes in a string of symbol pairs as a parameter
# The function should return true if the symbol string is balanced or False if it is not

# The String should only contain opening and closing symbols like "([{}])" or "(([{])"
# For symbols to be balanced, each opening symbol must also have a closing symbol, and
# the symbols must be properly nested
# Use stack in solution

def isSymbolStringBalanced(symbols):

    # implement hashmap for symbol pairs
    # keys are opening symbols and value is the matching closing symbol
    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    # going to need to check if each symbol was an opening symbol
    openers = symbol_pairs.keys()

    # using stack
    balancedStack = Stack()

    # iterator
    index = 0

    while index < len(symbols):
        # taking symbol at the index in the loop
        symbol = symbols[index]

        # checking to see if symbol is opening symbol
        if symbol in openers:
            # push symbol to stack
            balancedStack.push(symbol)
        else:
            # the symbol is a closer

            # if the stack is already empty, the symbols are not balanced
            if balancedStack.isEmpty():
                return False
            # if there are still items in the stack, check for a mis-match
            else:
                # pop most top item in stack
                top_item = balancedStack.pop()
                # check to see if it is a matching pair
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1

    if balancedStack.isEmpty():
        return True

    return False


print(isSymbolStringBalanced('([{}])'))
print(isSymbolStringBalanced('{([}))'))
