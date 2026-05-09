class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        count = 0
        self.prices.append(price)
        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices[i] <= price:
                count += 1
            else:
                break
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)



class StockSpanner:

    def __init__(self):
        self.stack = [] # pair (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))
        return span        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


class StockSpanner:

    def __init__(self):
        self.stack = []
        self.spans = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1] <= price:
            span += self.spans.pop()
            self.stack.pop()
        
        self.stack.append(price)
        self.spans.append(span)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)