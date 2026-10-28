from collections import deque

class MyStack:

    def __init__(self):
        # Initialize two queues using collections.deque
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # 1. Push the new element into the empty q2
        self.q2.append(x)

        # 2. Transfer all existing elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
            
        # 3. Swap q1 and q2 so q1 always holds the stack in LIFO order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # The front of q1 is always the top of the stack
        return self.q1.popleft()

    def top(self) -> int:
        # Peek at the front of q1 without removing it
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()