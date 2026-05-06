from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
    

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



class MyStack:

    def __init__(self):
        self.main = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.temp.append(x)
        while self.main:
            self.temp.append(self.main.popleft())
        self.temp, self.main = self.main, self.temp

    def pop(self) -> int:
        if self.main:
            return self.main.popleft()
        return -1

    def top(self) -> int:
        if self.main:
            return self.main[0]
        return -1

    def empty(self) -> bool:
        if len(self.main) != 0:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:

    def __init__(self):
        self.main = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.temp.append(x)
        while self.main:
            self.temp.append(self.main.popleft())
        self.temp, self.main = self.main, self.temp

    def pop(self) -> int:
        if self.main:
            return self.main.popleft()
        return -1

    def top(self) -> int:
        if self.main:
            return self.main[0]
        return -1

    def empty(self) -> bool:
        return not self.main
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()