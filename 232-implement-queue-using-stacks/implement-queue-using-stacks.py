class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Pushing is always O(1) onto the in_stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Ensure out_stack has the correct FIFO order
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        # If out_stack is empty, transfer all elements from in_stack, 
        # reversing their order to achieve FIFO behavior
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()