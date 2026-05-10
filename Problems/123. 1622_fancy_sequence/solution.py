class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.values = []
        self.mul = 1      
        self.add = 0      
        

    def append(self, val: int) -> None:
        normalized = (val - self.add) * self._mod_inverse(self.mul) % self.MOD
        self.values.append(normalized)
        
    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        return (self.values[idx] * self.mul + self.add) % self.MOD

    def _mod_inverse(self, a: int) -> int:
        return pow(a, self.MOD - 2, self.MOD)
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
