class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size > 0:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
            self.min_value = val
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.size > 0:
            value = self.stack.pop()
            self.size -= 1
            if value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.size > 0:
            return self.stack[-1]


    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return 0