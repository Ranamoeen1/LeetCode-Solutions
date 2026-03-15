class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.arr = []  # stores base values
        self.mul = 1   # current global multiplier
        self.add = 0   # current global addend
        
    def append(self, val: int) -> None:
        # base = (val - add) / mul = (val - add) * inv(mul) mod MOD
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        base = (val - self.add) * inv_mul % self.MOD
        self.arr.append(base)
        
    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD
        
    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)