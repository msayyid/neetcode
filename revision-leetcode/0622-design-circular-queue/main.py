class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k     

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        for i in range(len(self.queue)):
            if self.queue[i] == None:
                self.queue[i] = value
                return True


    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        for i in range(len(self.queue)):
            if self.queue[i] != None:
                self.queue[i] = None
                break
        for j in range(i, len(self.queue) - 1):
            self.queue[j] = self.queue[j + 1]
        self.queue[-1] = None
        return True

    def Front(self) -> int:
        for i in self.queue:
            if i != None:
                return i
        return -1
        

    def Rear(self) -> int:
        for i in range(len(self.queue) - 1, -1, -1):
            if self.queue[i] != None:
                return self.queue[i]
        return -1
        

    def isEmpty(self) -> bool:
        for i in self.queue:
            if i != None:
                return False
        return True
        

    def isFull(self) -> bool:
        for i in self.queue:
            if i == None:
                return False
        return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.rear = k - 1
        self.front = 0
        self.size = 0  
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size < self.k:
            # rear points to the last element
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            self.size += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.size > 0:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.k
            self.size -= 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.size > 0:
            return self.queue[self.front]
        return -1
        

    def Rear(self) -> int:
        if self.size > 0:
            return self.queue[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()