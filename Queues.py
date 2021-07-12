import random


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
            Takes in an item and inserts that item into the 0th index of the list
            that is representing the Queue

            The run time is O(n), or linear time, because inserting into the 0th
            index of a list forces all the other items to shift over one index to the right.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
            Returns and removes the front-most item of the queue, which is the last item in the list that represents the queue
            Runtime -> O(1) Constant time
        """
        if len(self.items) != 0:
            return self.items.pop()
        return None

    def peek(self):
        """
            Returns the last item in the list, but this is actually the first-most item in the queue
            Does not remove anything

            Runtime -> Constant O(1) because indexing into a list is done in constant time
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        Returns the size of the Queue, which is represented as the length of the list

        Runtime is O(1) or constant time, because we're only returning the length
        """
        return len(self.items)

    def isEmpty(self):
        """
        Returns true or false depending on whether the Queue is empty or not
        Runtime is Constant since we are just returning a boolean
        """
        return self.items == []


# Challenge
"""
    Create three classes that together model how a printer could take print jobs out of a print queue.
    First Class -> PrintQueue -> follows the queue data structure implementation. 
    Second Class -> Job -> has a pages attribute and each job can have one to 10 pages.
    You can assign this number randomly. Job class should also have a print page method that decrements pages
    and a check complete method which will check whether or not all the pages have been printed.
    Third Class -> Printer class.: -> should have a get job method that makes uses of the queues built in de-queue method
    to take the first job in the print queue off of the queue. Make sure to account for if the queue items is empty,
"""


class PrintQueue(Queue):
    def __init__(self):
        super().__init__()


class Job:
    def __init__(self):
        self.pages = None

    def setPages(self):
        self.pages = random.randint(1, 10)

    def printPage(self):
        if self.pages > 0:
            print(self.pages)
            self.pages -= 1

    def checkComplete(self):
        if self.pages == 0:
            return True
        return False


class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue: PrintQueue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No more jobs to print"

    def print_job(self, job: Job):
        while job.pages > 0:
            job.printPage()

        if job.checkComplete():
            return "Printing is complete"
        else:
            return "An error occurred"


job1 = Job()
job1.setPages()

print_queue = PrintQueue()
print_queue.enqueue(job1)

printer = Printer()
printer.get_job(print_queue)

printer.print_job(printer.current_job)
