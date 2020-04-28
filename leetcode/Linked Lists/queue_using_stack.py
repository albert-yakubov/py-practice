class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # one stack contains the items as they are added:
        self.stack = []
        # reverse stack is needed for pop operation
        self.reversed = []
        # top is the head for peek operation
        self.top = None 
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # basically if not in the stack yet
        if not self.stack:
            # start at the head:
            self.top = x
        # and append the rest of the values
        self.stack.append(x)        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # if not in reversed stack and is in the stack:
        if not self.reversed:
            while self.stack:
                # take the value from the stack and put it in reversed stack
                self.reversed.append(self.stack.pop())
                # and return the value popped
        return self.reversed.pop()
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.reversed:
            return self.reversed[-1]
        return self.top

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack and not self.reversed


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()