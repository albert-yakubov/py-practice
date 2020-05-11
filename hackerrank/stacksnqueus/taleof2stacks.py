class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        p = self.pop()
        self.second.append(p)
        return p

    def pop(self):
        if not self.second:
            [self.second.append(self.first.pop()) for i in range(len(self.first))]
        return self.second.pop()

    def put(self, value):
        self.first.append(value)