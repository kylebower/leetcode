class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxSize:
            self.stk.append(x)

    def pop(self) -> int:
        if len(self.stk)>0:
            return self.stk.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.stk))):
            self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)